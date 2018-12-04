function formatDate(d) {
  return `${d.getFullYear()}-${d.getMonth() + 1}-${d.getDate()}`
}

function isoToHumanReadable(isoString) {
  let time = new Date(isoString)
  return `${time.getFullYear()} 年 ${time.getMonth() + 1} 月 ${time.getDate()} 日`
}

function getGroupStage(procedure, stage) {
  for (let item of procedure) {
    if (item.stage === stage || item.stage + 1 === stage) {
      return item.name
    }
  }
  return '未知阶段'
}

function getContestStage(procedure, stage) {
  if (stage === 0) {
    return '尚未开始'
  } else if (stage === -1) {
    return '已经结束'
  } else {
    for (let item of procedure) {
      if (item.stage === stage) {
        return item.name + ' 进行中'
      } else if (item.stage + 1 === stage) {
        return item.name + ' 批改中'
      }
    }
    return '未知阶段'
  }
}

function isJudgeStage(stage) {
  return stage > 0 && stage % 2 === 0
}

function getPercentage(completed, all) {
  if (all === 0) {
    return 100
  }
  return Math.round((completed / all) * 100)
}

function isNullStage(stage) {
  return stage === 0 || stage === -1
}

function downloadFile(doc, src, filename = null) {
  let elementLink = doc.createElement('a')
  if (filename === null) {
    elementLink.download = src
  } else {
    elementLink.download = filename
  }
  elementLink.style.display = 'none'
  elementLink.href = src
  doc.body.appendChild(elementLink)
  elementLink.click()
  doc.body.removeChild(elementLink)
}

function guid() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = (Math.random() * 16) | 0,
      v = c === 'x' ? r : (r & 0x3) | 0x8
    return v.toString(16)
  })
}

export { formatDate, isoToHumanReadable, getGroupStage, getContestStage, isJudgeStage, getPercentage, isNullStage, downloadFile, guid }
