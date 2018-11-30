import json
from useraction.models import User
from django.test import TestCase, Client
from basic.models import Competition, CStage, Notice, Group, GStage, ReviewMeta, Vote


class MyClient(Client):

    def get(self, *args, **kwargs):
        response = super(MyClient, self).get(*args, **kwargs)
        return json.loads(response.content.decode())
        
    def post(self, *args, **kwargs):
        # 对于post来说，默认类型要是json
        if 'content_type' not in kwargs:
            kwargs['content_type'] = 'application/json'
        if 'data' in kwargs and kwargs.get('content_type') == 'application/json':
            kwargs['data'] = json.dumps(kwargs['data'])
        response = super(MyClient, self).post(*args, **kwargs)
        return json.loads(response.content.decode())
        
    def put(self, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        response = super(MyClient, self).put(*args, **kwargs)
        return json.loads(response.content.decode())
        
    def patch(self, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        response = super(MyClient, self).patch(*args, **kwargs)
        return json.loads(response.content.decode())
        
    def delete(self, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        response = super(MyClient, self).delete(*args, **kwargs)
        return json.loads(response.content.decode())


models = [User, Competition, CStage, Notice, Group, GStage, ReviewMeta, Vote]


def create_user(name):
    tmp = User.objects.filter(username=name)
    if not tmp:
        tmp = User.objects.create_user(username=name, password=name)
    else:
        tmp = tmp.first()
    tmp.save()
    globals()[name] = tmp
    return tmp
    

class BackendAPITest(TestCase):

    def setUp(self):
        # 创建这些用户并且释放到全局作用域中
        users = [create_user(x) for x in ['organizer', 'leader', 'student1', 'student2', 'reviewer1', 'admin']]
        organizer.individual = False
        organizer.save()

        # 变量 ``organizer``现在是包含用户名为``organizer``的浏览器
        for user in users:
            name = user.username
            tmp = MyClient()
            ans = tmp.login(username=name, password=name)
            globals()[name] = tmp

    def tearDown(self):
        pass
                
    def test_procedure(self):
        # 模拟一场比赛的流程
        
        # 主办方创建比赛
        data = {
            "charge": 0,
            "detail": "不存在的",
            "enrollEnd": "2018-12-01T16:00:00.000Z",
            "enrollForm": '12',
            "enrollStart": "2018-11-29T16:00:00.000Z",
            "enrollUrl": "",
            "groupSize": 1,
            "imgUrl": "url????",
            "name": "pwf",
            "procedure": [{"name": "初赛", "startTime": "2018-12-1", "endTime": "2018-12-3"},
                           {"name": "复赛", "startTime": "2018-12-4", "endTime": "2018-12-6"}],
            "publisher": "organizer",
            "subject": "pwf"
        }
        
        data = organizer.post('/api/contests', data)
        self.assertEqual(data['code'], 0)
        contest_id = data['data']['id']

        # 队长报名,并邀请student1参加
        data = leader.post(f'/api/contests/{contest_id}/enroll',
                           {"name":"无名", "leaderName":"leader", "members":["student1"], "form":"1"})
        self.assertEqual(data['code'], 0)
        group_id = data['data']['id']

        # 队长接着邀请student2参加
        data = leader.post(f'/apiv2/contests/{contest_id}/groups/{group_id}/invitenew',
                           {"username":"student2"})
        self.assertEqual(data['code'], 0)

        # student2同意了
        data = student2.post(f'/apiv2/contests/{contest_id}/groups/{group_id}/invitation',data={"accept":True})
        self.assertEqual(data['code'], 0)

        # student1拒绝了
        data = student1.post(f'/apiv2/contests/{contest_id}/groups/{group_id}/invitation',data={"accept":False})
        self.assertEqual(data['code'], 0)

        # 组长退出了
        data = leader.post(f'/apiv2/contests/{contest_id}/groups/{group_id}/quit')
        self.assertEqual(data['code'], 0)

        # student2成为了队长并且锁定了队伍
        data = student2.post(f'/apiv2/contests/{contest_id}/groups/{group_id}/lock')
        self.assertEqual(data['code'], 0)

        # 主办方添加评委
        data = organizer.post(f'/api/contests/{contest_id}/reviewer', {'username':['reviewer1']})
        self.assertEqual(data['code'], 0)

        # 两个阶段
        for stage in range(1, 3):

            # 主办方宣布进入下一个阶段
            data = organizer.post(f'/api/contests/{contest_id}', data={'stage':2 * stage - 1})
            self.assertEqual(data['code'], 0)

            # 选手提交, 太难用代码测试，直接改数据库
            group = Group.objects.get(id=group_id)
            group_stage = group.stage_list.get(stage=group.current_stage)
            group_stage.commit_path = '/a/b/c.txt'
            group_stage.submission = 'ddd'
            group_stage.has_commit = True
            group_stage.save()

            # 主办方宣布进入评审阶段
            data = organizer.post(f'/api/contests/{contest_id}', data={'stage':2 * stage})
            self.assertEqual(data['code'], 0)

            # 主办方分配任务
            data = organizer.post(f'/api/contests/{contest_id}/auto_assign',
                                  data={'stage':2 * stage, "serious":True, "maxconn":3, "judges":[{"username":"reviewer1", "assign":3}]})
            self.assertEqual(data['code'], 0)

            # 评委查看其任务
            data = reviewer1.get(f'/api/judges/{contest_id}', data={'stage':2 * stage})
            self.assertEqual(data['code'], 0)
            review_meta_id = data['data']['submissions'][0]['id']

            # 评委打分
            data = reviewer1.post(f'/api/judges/{contest_id}', data={'reviews':[{
              "id": review_meta_id,
              "reviewed": True,
              "rating": 80,
              "msg": "不错"}]})
            self.assertEqual(data['code'], 0)

            # 主办方晋级队伍
            data = organizer.post(f'/api/contests/{contest_id}/groups', data={'stage':2 * stage + 1, "group_ids":[group_id]})
            self.assertEqual(data['code'], 0)

        # 比赛结束
        return