import request from '@/plugin/axios'

export function InterviewsRecord (data) {
  return request({
    url: 'http://47.95.8.112:9877/qyburn/prescription/c',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    method: 'get',
    params: data
  })
}

export function InterviewsRecordIn (data) {
  return request({
    url: 'http://47.95.8.112:9877/qyburn/prescription/u',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    method: 'get',
    params: data
  })
}
