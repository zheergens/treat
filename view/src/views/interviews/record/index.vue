<template>
  <d2-container>
    <el-row :gutter="20">
        <el-col :span="7">
            <el-autocomplete class="input-demo-200" v-model="userName" :fetch-suggestions="querySearch" placeholder="请输入内容"
              :trigger-on-focus="false">
              <el-select v-model="action" slot="prepend" placeholder="请选择" style="width: 90px;">
                <el-option label="姓名" value="user_name"></el-option>
                <el-option label="身份证" value="carded"></el-option>
                <el-option label="电话号" value="phone_num"></el-option>
              </el-select>
              <el-button slot="append" icon="el-icon-search" @click="searchF"></el-button>
            </el-autocomplete>
        </el-col>
        <el-col :span="6">
            <h2 align="right"> 当前患者: &nbsp;&nbsp;{{ user_name }} </h2>
        </el-col>
        <el-col :span="12"></el-col>
    </el-row>
    <el-row v-if="show" class="demo-autocomplete" :gutter="10">
      <el-col :span="2">
        <span class="d2-mt-0">姓名</span>
      </el-col>
      <el-col :span="6">
        {{ user_name }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="2"></el-col>
      <el-col :span="2">
        <span class="d2-mt-0">性别</span>
      </el-col>
      <el-col :span="2">
        {{ sex }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="2"></el-col>
      <el-col :span="2">
        <span class="d2-mt-0">年龄</span>
      </el-col>
      <el-col :span="6">
        {{ age }}
        <el-divider></el-divider>
      </el-col>
    </el-row>
    <el-row v-if="show" class="demo-autocomplete" :gutter="10">
      <el-col :span="2">
      <span class="d2-mt-0">身份证号</span>
      </el-col>
      <el-col :span="6">
        {{ carded }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="8"></el-col>
      <el-col :span="2">
      <span class="d2-mt-0">联系电话</span>
      </el-col>
      <el-col :span="6">
        {{ phone_num }}
        <el-divider></el-divider>
      </el-col>
    </el-row>
    <el-row v-if="show" class="demo-autocomplete" :gutter="10">
      <el-col :span="2">
      <span class="d2-mt-0">详细地址</span>
      </el-col>
      <el-col :span="6">
        {{ address }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="8"></el-col>
      <el-col :span="2">
        <span class="d2-mt-0">科别</span>
      </el-col>
      <el-col :span="6">
        {{ department }}
        <el-divider></el-divider>
      </el-col>
    </el-row>
    <el-row v-if="show" class="demo-autocomplete" :gutter="10">
      <el-col :span="2">
        <span class="d2-mt-0">就诊医院</span>
      </el-col>
      <el-col :span="6">
        {{ hospital }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="8"></el-col>
      <el-col :span="2">
        <span class="d2-mt-0">医疗证号</span>
      </el-col>
      <el-col :span="6">
        {{ medical_certificate_number }}
        <el-divider></el-divider>
      </el-col>
    </el-row>
    <el-row v-if="show" class="demo-autocomplete" :gutter="10">
      <el-col :span="14">
        <span class="d2-mt-0">临床诊断 (症状 空格隔开)</span>
        <el-input type="textarea" class="input-demo-200" v-model="diagnosis"></el-input>
      </el-col>
    </el-row>
    <el-row v-if="show" class="demo-autocomplete" :gutter="10">
      <el-col :span="14">
        <span class="d2-mt-0">药方 (菊花100g 空格隔开)</span>
        <el-input type="textarea" rows="3" class="input-demo-200" v-model="prescription"></el-input>
      </el-col>
    </el-row>
    <br/>
    <el-row v-if="show" class="demo-autocomplete" :gutter="10">
      <el-col :span="2">
        <span class="d2-mt-0">医师</span>
      </el-col>
      <el-col :span="4">
        {{ physician }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="2">
        <span class="d2-mt-0">校验药师</span>
      </el-col>
      <el-col :span="4">
        {{ pharmacist }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="2">
        <span class="d2-mt-0">收费员</span>
      </el-col>
      <el-col :span="4">
        {{ toll_collector }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="2">
        <span class="d2-mt-0">审核</span>
      </el-col>
      <el-col :span="4">
        {{ reviewed }}
        <el-divider></el-divider>
      </el-col>
    </el-row>
    <el-row v-if="show" class="demo-autocomplete" :gutter="10">
      <el-col :span="2">
        <span class="d2-mt-0">药费</span>
      </el-col>
      <el-col :span="4">
        {{ drug_fee }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="2">
        <span class="d2-mt-0">检查费</span>
      </el-col>
      <el-col :span="4">
        {{ inspection_fee }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="2">
        <span class="d2-mt-0">处置费</span>
      </el-col>
      <el-col :span="4">
        {{ disposal_fee }}
        <el-divider></el-divider>
      </el-col>
      <el-col :span="2">
        <span class="d2-mt-0">优惠费用</span>
      </el-col>
      <el-col :span="4">
        {{ preferential }}
        <el-divider></el-divider>
      </el-col>
    </el-row>
    <br/>
    <el-row v-if="show">
        <el-col :span="8"></el-col>
        <el-col :span="8">
          <el-button-group>
            <el-button type="primary" icon="el-icon-arrow-left" @click="pageReduce">上一页</el-button>
            <el-button type="primary" @click="pageAdd">下一页<i class="el-icon-arrow-right el-icon--right"></i></el-button>
          </el-button-group>
        </el-col>
        <el-col :span="8"></el-col>
    </el-row>
  </d2-container>
</template>

<style scoped>
 .el-col{
  min-height: 40px;
 }
 .el-row{
  margin-bottom: 8px;
 }
 .d2-mt-0{
  display: inline-block;
  line-height: 40px;
 }
</style>

<script>
import { InterviewsRecord } from '@/api/interviews/record/'

export default {
  name: 'interviews-record',
  data: function () {
    return {
      userName: '',
      action: 'user_name',
      userInfo: '',
      show: false,
      citys: '',
      user_name: '',
      carded: '',
      sex: '',
      age: 0,
      address_detail: '',
      hospital: '',
      address: '',
      phone_num: '',
      department: '',
      medical_certificate_number: '',
      diagnosis: '',
      prescription: '',
      physician: '',
      pharmacist: '',
      toll_collector: '',
      reviewed: '',
      drug_fee: 0,
      inspection_fee: 0,
      disposal_fee: 0,
      preferential: 0,
      departmentOptions: '',
      physicianOptions: '',
      pharmacistOptions: '',
      collectorOptions: '',
      reviewedOptions: '',
      page: 0,
      restaurants: [
        { value: '陈波', address: '陈波' }
      ]
    }
  },
  methods: {
    searchF: function() {
      this.page = 0
      this.onSubmit()
    },
    onSubmit: function () {
      if (this.userName === '') {
        this.$message({
          message: '输入查询参数',
          type: 'error'
        }) 
        return
      }
      this.show = true,
      InterviewsRecord({
        key: this.action,
        value: this.userName,
        page: this.page
      })
        .then(res => {
          this.userInfo = res[0]
          if (res.length === 0) {
            this.$message({
              message: '没有信息了哦！',
              type: 'error'
            }) 
          }
          this.user_name = this.userInfo.user_name
          this.carded = this.userInfo.carded
          if (this.userInfo.sex === '1') {
            this.sex = '男'
          } else {
            this.sex = '女'
          }
          this.age = this.userInfo.age
          this.address = this.userInfo.address
          this.address_detail = this.userInfo.address_detail
          this.hospital = this.userInfo.hospital
          this.phone_num = this.userInfo.phone_num
          this.department = this.userInfo.department
          this.medical_certificate_number = this.userInfo.medical_certificate_number
          this.diagnosis = this.userInfo.diagnosis
          this.prescription = this.userInfo.prescription
          this.physician = this.userInfo.physician
          this.pharmacist = this.userInfo.pharmacist
          this.toll_collector = this.userInfo.toll_collector
          this.reviewed = this.userInfo.reviewed
          this.drug_fee = this.userInfo.drug_fee
          this.inspection_fee = this.userInfo.inspection_fee
          this.disposal_fee = this.userInfo.disposal_fee
          this.preferential = this.userInfo.preferential
          this.department = this.userInfo.department
          this.physician = this.userInfo.physician
          this.reviewed = this.userInfo.reviewed
        })
    },
    pageReduce: function() {
      this.$log.primary(this.page)
      this.page = this.page - 1

      //Object.assign(this.$data, this.$options.data())
      //this.userName = 
      //this.page = 
      this.onSubmit()
    },
    pageAdd: function() {
      this.$log.primary(this.page)
      this.page = this.page + 1
     // Object.assign(this.$data, this.$options.data())
      this.$log.primary(0)
      this.onSubmit()
    },
    handleSelect (item) {
      console.log(item)
    },
    getIndexes() {
      this.restaurants = []       
    },
    querySearch (queryString, cb) {
      var restaurants = this.restaurants
      var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants
      // 调用 callback 返回建议列表的数据
      cb(results)
    },
    createFilter (queryString) {
      return (restaurant) => {
        return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0)
      }
    }
  }
}
</script>
