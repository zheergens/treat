<template>
  <d2-container>
    <el-row class="demo-autocomplete" :gutter="10">
      <el-col :span="2">
        <span class="d2-mt-0">姓名</span>
      </el-col>
      <el-col :span="4">
        <el-input class="input-demo-200" v-model="user_name" placeholder="张三"></el-input>
      </el-col>
      <el-col :span="2"></el-col>
      <el-col :span="2">
        <span class="d2-mt-0">性别</span>
      </el-col>
      <el-col :span="6">
        <el-radio v-model="sex" label="1">男</el-radio>
        <el-radio v-model="sex" label="2">女</el-radio>
      </el-col>
      <el-col :span="2">
        <span class="d2-mt-0">年龄</span>
      </el-col>
      <el-col :span="6">
        <el-input-number v-model="age" :step="1"></el-input-number>
      </el-col>
    </el-row>
    <el-row class="demo-autocomplete" :gutter="10">
	    <el-col :span="2">
		  <span class="d2-mt-0">身份证号</span>
	    </el-col>
	    <el-col :span="6">
		  <el-input class="input-demo-200" v-model="carded" placeholder="522xxxxxxx"></el-input>
	    </el-col>
	    <el-col :span="8"></el-col>
	    <el-col :span="2">
		  <span class="d2-mt-0">联系电话</span>
	    </el-col>
	    <el-col :span="6">
		  <el-input class="input-demo-200" v-model="phone_num" placeholder="156529xxxxx"></el-input>
	    </el-col>
	  </el-row>
	  <el-row class="demo-autocomplete" :gutter="10">
	    <el-col :span="2">
		  <span class="d2-mt-0">所在区</span>
	    </el-col>
	    <el-col :span="8">
		    <el-cascader size="large" :options="citys" v-model="address"></el-cascader>
	    </el-col>
	    <el-col :span="6"></el-col>
	    <el-col :span="2">
		    <span class="d2-mt-0">详细地址</span>
	    </el-col>
	    <el-col :span="6">
		    <el-input class="input-demo-200" v-model="address_detail" placeholder="亮马桥九号院一号楼"></el-input>
	    </el-col>
	  </el-row>
	  <el-row class="demo-autocomplete" :gutter="10">
	    <el-col :span="2">
		    <span class="d2-mt-0">就诊医院</span>
	    </el-col>
	    <el-col :span="6">
		    <el-input class="input-demo-200" v-model="hospital" placeholder="中日友好医院"></el-input>
	    </el-col>
	    <el-col :span="2">
		    <span class="d2-mt-0">科别</span>
	    </el-col>
	    <el-col :span="6">
		    <el-select v-model="department" placeholder="请选择">
		      <el-option v-for="item in departmentOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
		    </el-select>
	    </el-col>
	    <el-col :span="2">
		    <span class="d2-mt-0">医疗证号</span>
	    </el-col>
	    <el-col :span="6">
		    <el-input class="input-demo-200" v-model="medical_certificate_number" placeholder="952782632xxxxxxx"></el-input>
	    </el-col>
	  </el-row>
	  <el-row class="demo-autocomplete" :gutter="10">
	    <el-col :span="14">
		    <span class="d2-mt-0">临床诊断</span>
	      <el-input type="textarea" class="input-demo-200" v-model="diagnosis" placeholder="发热,头疼"></el-input>
	    </el-col>
	  </el-row>
	  <el-row class="demo-autocomplete" :gutter="10">
	    <el-col :span="14">
		    <span class="d2-mt-0">药方</span>
		    <el-input type="textarea" rows="3" class="input-demo-200" v-model="prescription" placeholder="藏红花:100g, 陈皮:10g,"></el-input>
	    </el-col>
	  </el-row>
    <br/><br/>
	  <el-row class="demo-autocomplete" :gutter="10">
	    <el-col :span="2">
		    <span class="d2-mt-0">医师</span>
	    </el-col>
	    <el-col :span="4">
		    <el-select v-model="physician" placeholder="请选择">
		      <el-option v-for="item in physicianOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
		    </el-select>
	    </el-col>
	    <el-col :span="2">
		    <span class="d2-mt-0">校验药师</span>
      </el-col>
	    <el-col :span="4">
		    <el-select v-model="pharmacist" placeholder="请选择">
		      <el-option v-for="item in pharmacistOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
		    </el-select>
	    </el-col>
	    <el-col :span="2">
		    <span class="d2-mt-0">收费员</span>
	    </el-col>
	    <el-col :span="4">
		    <el-select v-model="toll_collector" placeholder="请选择">
		      <el-option v-for="item in collectorOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
		    </el-select>
	    </el-col>
	    <el-col :span="2">
		    <span class="d2-mt-0">审核</span>
	    </el-col>
	    <el-col :span="4">
		    <el-select v-model="reviewed" placeholder="请选择">
		      <el-option v-for="item in reviewedOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
		    </el-select>
	    </el-col>
	  </el-row>
	  <el-row class="demo-autocomplete" :gutter="10">
	    <el-col :span="2">
		    <span class="d2-mt-0">药费</span>
	    </el-col>
	    <el-col :span="4">
		    <el-input class="input-demo-200" v-model="drug_fee" placeholder="0"></el-input>
	    </el-col>
	    <el-col :span="2">
		    <span class="d2-mt-0">检查费</span>
	    </el-col>
	    <el-col :span="4">
		    <el-input class="input-demo-200" v-model="inspection_fee" placeholder="0"></el-input>
	    </el-col>
	    <el-col :span="2">
        <span class="d2-mt-0">处置费</span>
      </el-col>
      <el-col :span="4">
        <el-input class="input-demo-200" v-model="disposal_fee" placeholder="0"></el-input>
      </el-col>
      <el-col :span="2">
        <span class="d2-mt-0">优惠费用</span>
      </el-col>
      <el-col :span="4">
        <el-input class="input-demo-200" v-model="preferential" placeholder="0"></el-input>
      </el-col>
    </el-row>
    <br/>
    <el-row class="demo-autocomplete" style="text-align:right;">
      <el-button type="primary" :plain="true" @click="onSubmit()">提交</el-button>
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
import { regionDataPlus, CodeToText } from 'element-china-area-data'
import { InterviewsRecordIn } from '@/api/interviews/record/'

export default {
  name: 'treat-prescription',
  data () {
    return {
      show: false,
      citys: regionDataPlus,
      user_name: '',
      carded: '',
      sex: '1',
      age: 18,
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
      departmentOptions: [{
        value: '急诊科',
        label: '急诊科'
      },
      {
        value: '内科',
        label: '内科'
      },
      {
        value: '外科',
        label: '外科'
      },
      {
        value: '妇产科',
        label: '妇产科'
      },
      {
        value: '眼科',
        label: '眼科'
      },
      {
        value: '耳鼻喉科',
        label: '耳鼻喉科'
      },
      {
        value: '口腔科',
        label: '口腔科'
      },
      {
        value: '中医科',
        label: '中医科'
      },
      {
        value: '皮肤科',
        label: '皮肤科'
      },
      {
        value: '麻醉科',
        label: '麻醉科'
      },
      {
        value: '康复科',
        label: '康复科'
      },
      {
        value: '预防保健科',
        label: '预防保健科'
      },
      {
        value: '神经内科',
        label: '神经内科'
      },
      {
        value: '儿科',
        label: '儿科'
      }],
      physicianOptions: [{
        value: '冯主任',
        label: '冯主任'
      },
      {
        value: '薛医生',
        label: '薛医生'
      }],
      pharmacistOptions: [{
        value: '冯主任',
        label: '冯主任'
      },
      {
        value: '薛医生',
        label: '薛医生'
      }],
      collectorOptions: [{
        value: '冯主任',
        label: '冯主任'
      },
      {
        value: '薛医生',
        label: '薛医生'
      }],
      reviewedOptions: [{
        value: '冯主任',
        label: '冯主任'
      },
      {
        value: '薛医生',
        label: '薛医生'
      }]
    }
  },
  methods: {
    onSubmit: function () {
      var dt = this.address
      var local = ''
      for (var prop in dt) {
        this.$log.primary(CodeToText[dt[prop]])
        local += CodeToText[dt[prop]]
      }
      this.address = local + this.address_detail
      this.$log.primary(this.address)
      var info = {
        user_name: this.user_name,
        carded: this.carded,
        sex: this.sex,
        age: this.age,
        hospital: this.hospital,
        address: this.address,
        phone_num: this.phone_num,
        department: this.department,
        medical_certificate_number: this.medical_certificate_number,
        diagnosis: this.diagnosis,
        prescription: this.prescription,
        physician: this.physician,
        pharmacist: this.pharmacist,
        toll_collector: this.toll_collector,
        reviewed: this.reviewed,
        drug_fee: this.drug_fee,
        inspection_fee: this.inspection_fee,
        disposal_fee: this.disposal_fee,
        preferential: this.preferential
      }
      this.$log.primary(info)
      InterviewsRecordIn(info)
      var messagex
      var typex 
      if (this.user_name === '') {
        messagex = '请输入信息'
        typex = 'warning'
      } else {
        messagex = '录入成功'
        typex = 'success'
      }
      this.$message({
          message: messagex,
          type: typex
       })
      Object.assign(this.$data, this.$options.data())
    }
  }
}
</script>
