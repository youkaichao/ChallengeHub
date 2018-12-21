#include <Python.h>

int *team_tokens, *judge_tokens, *judge_bottlenecks;
int team_size, judge_size;
int max_conn, use_token;


static PyObject *set_max_conn(PyObject *self, PyObject *args) {
    if (!PyArg_ParseTuple(args, "i", &max_conn)) {
        PyErr_SetString(PyExc_TypeError, "int max_conn");
        return NULL;
    }
    return Py_None;
}

static PyObject *set_use_token(PyObject *self, PyObject *args) {
    if (!PyArg_ParseTuple(args, "i", &use_token)) {
        PyErr_SetString(PyExc_TypeError, "int use_token");
        return NULL;
    }
    return Py_None;
}


static PyObject *set_team_size(PyObject *self, PyObject *args) {
    if (!PyArg_ParseTuple(args, "i", &team_size)) {
        PyErr_SetString(PyExc_TypeError, "int team_size");
        return NULL;
    }
    return Py_None;
}

static PyObject *set_judge_size(PyObject *self, PyObject *args) {
    if (!PyArg_ParseTuple(args, "i", &judge_size)) {
        PyErr_SetString(PyExc_TypeError, "int judge_size");
        return NULL;
    }
    return Py_None;
}

static PyObject *set_team_tokens(PyObject *self, PyObject *py_teams) {
    Py_ssize_t tmp_size = PyList_Size(py_teams);
    if (tmp_size != team_size) {
        PyErr_SetString(PyExc_IndexError, "team size do not match!");
        return NULL;
    }
    if (team_tokens) {
        free(team_tokens);
        team_tokens = NULL;
    }
    team_tokens = malloc(sizeof(int) * team_size);
    int i;
    for (i = 0; i < team_size; i++) {
        PyObject *item = PyList_GetItem(py_teams, i);
        long value = PyLong_AsLong(item);
        team_tokens[i] = (int) value;
    }
    return Py_None;
}


static PyObject *set_judge_tokens(PyObject *self, PyObject *py_judges) {
    Py_ssize_t tmp_size = PyList_Size(py_judges);
    if (tmp_size != judge_size) {
        PyErr_SetString(PyExc_IndexError, "judge size do not match!");
        return NULL;
    }
    if (judge_tokens) {
        free(judge_tokens);
        judge_tokens = NULL;
    }
    judge_tokens = malloc(sizeof(int) * judge_size);
    int i;
    for (i = 0; i < judge_size; i++) {
        PyObject *item = PyList_GetItem(py_judges, i);
        long value = PyLong_AsLong(item);
        judge_tokens[i] = (int) value;
    }
    return Py_None;
}


static PyObject *set_judge_bottlenecks(PyObject *self, PyObject *py_bottlenecks) {
    Py_ssize_t tmp_size = PyList_Size(py_bottlenecks);
    if (tmp_size != judge_size) {
        PyErr_SetString(PyExc_IndexError, "judge size do not match!");
        return NULL;
    }
    if (judge_bottlenecks) {
        free(judge_bottlenecks);
        judge_bottlenecks = NULL;
    }
    judge_bottlenecks = malloc(sizeof(int) * judge_size);
    int i;
    for (i = 0; i < judge_size; i++) {
        PyObject *item = PyList_GetItem(py_bottlenecks, i);
        long value = PyLong_AsLong(item);
        judge_bottlenecks[i] = (int) value;
    }
    return Py_None;
}

#define maxn 10010
#define maxm 200010

int head[maxn], nxt[maxm], to[maxm], cap[maxm], from[maxm], tot;

void clear(void) {
    memset(head, 0, sizeof(head));
    tot = 1;
}

void _add(int u, int v, int w) {
    to[++tot] = v;
    from[tot] = u;
    nxt[tot] = head[u];
    head[u] = tot;
    cap[tot] = w;
}

void add_edge(int u, int v, int w) {
    _add(u, v, w);
    _add(v, u, w);
}

int d[maxn], cur[maxn];
int n, s, t;

int q[maxn], qh, qt;

int bfs(void) {
    qh = qt = 0;
    int i;
    for (i = 0; i < n; i++) {
        d[i] = -1;
    }
    d[s] = 0;
    q[qt++] = s;
    while (qh < qt) {
        int u = q[qh++];
        int k;
        for (k = head[u]; k; k = nxt[k]) {
            int v = to[k];
            if (cap[k] != 0 && d[v] == -1) {
                d[v] = d[u] + 1;
                q[qt++] = v;
            }
        }
    }
    return d[t] != -1;
}

#define min(a, b) ((a)>(b)?(b):(a))
#define INF 0x3f3f3f3f

int dfs(int x, int y) {
    if (x == t || !y) {
        return y;
    }
    int z = y;
    int k, v;
    for (k = cur[x]; k; cur[x] = k = nxt[k]) {
        if (cap[k] && d[v = to[k]] == d[x] + 1) {
            int w = dfs(v, min(cap[k], z));
            cap[k] -= w;
            cap[k ^ 1] += w; // NOLINT
            z -= w;
            if (!z) {
                break;
            }
        }
    }
    if (z == y) {
        d[x] = -1;
    }
    return y - z;
}

int max_flow(int _s, int _t) {
    s = _s;
    t = _t;
    int flow = 0;
    while (bfs()) {
        int i;
        for (i = 0; i < n; i++) {
            cur[i] = head[i];
        }
        flow += dfs(s, INF);
    }
    return flow;
}

#define S_num() 0
#define T_num() 1
#define Judge_num(i) (2+(i))
#define Team_num(i) (2+(judge_size)+(i))
#define Total() (2+(judge_size)+(team_size))
#define Judge_reverse(x) ((x)-2)
#define Team_reverse(x) ((x)-(judge_size)-2)

static PyObject *network_flow(PyObject *self, PyObject *noargs) {
    n = Total();
    clear();

    int i, j;
    for (i = 0; i < judge_size; i++) {
        add_edge(S_num(), Judge_num(i), judge_bottlenecks[i]);
    }
    for (i = 0; i < team_size; i++) {
        add_edge(Team_num(i), T_num(), max_conn);
    }
    int cur_edge = tot;
    for (i = 0; i < judge_size; i++) {
        for (j = 0; j < team_size; j++) {
            if (!use_token || judge_tokens[i] != team_tokens[j]) {
                add_edge(Judge_num(i), Team_num(j), 1);
            }
        }
    }
    max_flow(S_num(), T_num());

    PyObject *res = PyList_New(0);
    for (i = 0; i < judge_size; i++) {
        PyObject *tmp = PyList_New(0);
        PyList_Append(res, tmp);
    }
    for (i = cur_edge + 1; i <= tot; i += 2) {
        int u = Judge_reverse(from[i]);
        int v = Team_reverse(to[i]);
        int w = cap[i];
        if (w == 0) {
            PyObject *tmp = PyList_GetItem(res, u);
            PyList_Append(tmp, PyLong_FromLong(v));
        }
    }
    return res;
}


static PyMethodDef flowMethods[] = {
        {"set_max_conn",          set_max_conn,          METH_VARARGS, ""},
        {"set_use_token",         set_use_token,         METH_VARARGS, ""},
        {"set_team_size",         set_team_size,         METH_VARARGS, ""},
        {"set_judge_size",        set_judge_size,        METH_VARARGS, ""},
        {"set_team_tokens",       set_team_tokens,       METH_O,       ""},
        {"set_judge_tokens",      set_judge_tokens,      METH_O,       ""},
        {"set_judge_bottlenecks", set_judge_bottlenecks, METH_O,       ""},
        {"network_flow",          network_flow,          METH_NOARGS,  ""},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cModPyDem = {
        PyModuleDef_HEAD_INIT,
        "libflow",
        "network flow to assign contestants to reviewers",
        -1,
        flowMethods
};

PyMODINIT_FUNC PyInit_libflow(void) {
    return PyModule_Create(&cModPyDem);
}