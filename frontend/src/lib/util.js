function formatDate(d) {
  return `${d.getFullYear()}-${d.getMonth() + 1}-${d.getDate()}`
}

function isoToHumanReadable (isoString) {
  let time = new Date(Date.parse(isoString))
  return `${time.getFullYear()} 年 ${time.getMonth()} 月 ${time.getDate()} 日`
}
export { formatDate, isoToHumanReadable }
