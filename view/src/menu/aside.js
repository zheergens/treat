// 菜单 侧边栏
export default [
  { title: '首页', icon: 'home', path: '/index' },
  {
    title: '病人',
    icon: 'wheelchair',
    children: [
      { path: '/interviews/record', title: '问诊记录', icon: 'hospital-o' },
    ]
  },
  {
    title: '开方',
    icon: 'stethoscope',
    children: [
      { path: '/treat/prescription', title: '病症开方', icon: 'medkit' },
      { path: '/treat/drug', title: '中药特性', icon: 'envira' }
    ]
  }
]
