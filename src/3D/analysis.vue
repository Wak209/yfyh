<template>
    <br><br>
    <el-row>
      <el-col :span="5">
        <el-tooltip content="预计时长：半分钟" placement="bottom" effect="light">
          <el-button class="button" @click="handleclick" round type="primary">分析</el-button>
        </el-tooltip>
      </el-col>
      <p style="color:cornflowerblue">"健康程度"仅供参考，请以医生建议为准</p>
    </el-row>
    <br>

    <!--el-col :span="10"-->
    <el-table
    class="Table"
    :data="tableData"
    :key="certin"
    style="width: 70%"
    @row-click="editCurrentApplicationApproval"
  >
    <el-table-column prop="name" label="器官"  width="100" />
      <!-- eslint-disable-next-line-->
      <!--template slot-scope="scope">
        <a @click="" style="color:blue;cursor:pointer">{{scope.row}}</a>
      </template-->
    <el-table-column prop="id" label="标签值" width="100"  sortable/>
    <el-table-column prop="num" label="体积" width="150" sortable />
    <el-table-column prop="Xlen" label="直径(X)" width="100" sortable />
    <el-table-column prop="Ylen" label="直径(Y)" width="100" sortable />
    <el-table-column prop="Zlen" label="直径(Z)" width="100" sortable />
    <el-table-column prop="XS" label="横截面(X)" width="120" sortable />
    <el-table-column prop="YS" label="横截面(Y)" width="120" sortable />
    <el-table-column prop="ZS" label="横截面(Z)" width="120" sortable />
    <el-table-column prop="p" label="健康程度（仅供参考）" width="200" sortable/>
  </el-table>
  <!--/el-col-->
  <!--el-col :span="2"></el-col>
  <el-col :span="8">
    <div  class="border" style="border:dashed;border-radius: 4px; box-shadow: 12px 12px 12px rgba(0,0,0,0.1);border-width: thin">
        <div v-show="shownum==='无'"><p>等待数据...</p></div>
        <div v-show="shownum==='脾脏'"><p>1</p></div>
        <div v-show="shownum==='胆囊'"><p>2</p></div>
    </div>
  </el-col-->
  <!--div  class="border" style="border:dashed;border-radius: 4px; box-shadow: 12px 12px 12px rgba(0,0,0,0.1);border-width: thin">
    <div v-show="shownum==='无'"><p>等待数据...</p></div>
    <div v-show="shownum==='脾脏'"><p>脾脏是一个位于左上腹部的器官，它有助于身体对红血球进行过滤和分解，同时也是免疫系统的一部分，负责产生和储存淋巴细胞和抗体。常见的脾脏疾病包括脾梗死、脾功能亢进、脾肿大等。</p></div>
    <div v-show="shownum==='胆囊'"><p>胆囊是一个位于肝脏下方的小囊状器官，主要功能是储存由肝脏产生的胆汁，当身体需要时，胆囊会将胆汁释放到小肠中，帮助消化脂肪。常见的胆囊疾病包括胆囊结石、胆囊炎、胆囊切除术等。</p></div>
    <div v-show="shownum==='右肾'"><p>肾脏是人体内最重要的器官之一，主要功能是过滤血液，排除废物和过多的水分，并产生尿液。右肾和左肾位于腹腔内两侧，右肾比左肾略低，两者大小和功能相似。常见的肾脏疾病包括肾结石、肾囊肿、肾炎、肾衰竭等。</p></div>
    <div v-show="shownum==='左肾'"><p>肾脏是人体内最重要的器官之一，主要功能是过滤血液，排除废物和过多的水分，并产生尿液。右肾和左肾位于腹腔内两侧，右肾比左肾略低，两者大小和功能相似。常见的肾脏疾病包括肾结石、肾囊肿、肾炎、肾衰竭等。</p></div>
    <div v-show="shownum==='食管'"><p>食管是一条管状结构，连接口腔和胃，负责将食物运输到胃中。常见的食管疾病包括食管癌、食管炎、食管溃疡等。</p></div>
    <div v-show="shownum==='肝脏'"><p>肝脏是人体内最大的内脏器官之一，负责合成胆汁、代谢药物和毒素、储存能量等。常见的肝脏疾病包括肝炎、肝硬化、脂肪肝等。</p></div>
    <div v-show="shownum==='胃'"><p>胃是一个位于腹部的J形器官，主要功能是消化食物。常见的胃部疾病包括胃溃疡、胃癌、胃炎等。</p></div>
    <div v-show="shownum==='主动脉'"><p>主动脉和下腔动脉是人体内两条最大的血管，分别负责将氧和营养物质输送到全身组织和器官。常见的动脉疾病包括动脉硬化、动脉瘤、动脉闭塞等。</p></div>
    <div v-show="shownum==='下腔动脉'"><p>主动脉和下腔动脉是人体内两条最大的血管，分别负责将氧和营养物质输送到全身组织和器官。常见的动脉疾病包括动脉硬化、动脉瘤、动脉闭塞等。</p></div>
    <div v-show="shownum==='胰腺'"><p>胰腺是一个位于腹部的长形腺体，主要功能是产生胰液和激素，帮助消化食物和调节血糖水平。常见的胰腺疾病包括胰腺炎、胰腺癌等。</p></div>
    <div v-show="shownum==='右肾上腺'"><p>肾上腺是一对小腺体，位于肾脏上方，主要分泌肾上腺素和去甲肾上腺素，调节身体的代谢和应激反应。常见的肾上腺疾病包括肾上腺功能亢进症、肾上腺皮质功能减退症等。</p></div>
    <div v-show="shownum==='左肾上腺'"><p>肾上腺是一对小腺体，位于肾脏上方，主要分泌肾上腺素和去甲肾上腺素，调节身体的代谢和应激反应。常见的肾上腺疾病包括肾上腺功能亢进症、肾上腺皮质功能减退症等。</p></div>
    <div v-show="shownum==='十二指肠'"><p>十二指肠是一段位于胃和小肠之间的结肠，主要功能是将胆汁和胰液分泌到小肠中，帮助消化和吸收营养。常见的十二指肠疾病包括十二指肠溃疡、十二指肠癌等。</p></div>
    <div v-show="shownum==='膀胱'"><p>膀胱是一个储存尿液的器官，位于盆腔底部。常见的膀胱疾病包括膀胱炎、膀胱结石、膀胱癌等。膀胱的正常功能需要神经、肌肉和泌尿系统的协调工作。</p></div>
    <div v-show="shownum==='前列腺/子宫'"><p>前列腺是男性生殖系统的一部分，位于膀胱下方，主要分泌前列腺液，帮助维持精液的液态。常见的前列腺疾病包括前列腺炎、前列腺增生、前列腺癌等。子宫是女性生殖系统的一部分，位于盆腔内，主要功能是容纳和孕育胎儿。常见的子宫疾病包括子宫肌瘤、子宫内膜异位症、子宫癌等。子宫还参与了月经周期的调节和生殖激素的代谢。</p></div>
  </div-->
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>{{shownum}}</span>
      </div>
    </template>
    <div v-show="shownum==='器官名称'"><p>请点击表格查看</p></div>
    <div v-show="shownum==='脾脏'"><p>脾脏是一个位于左上腹部的器官，它有助于身体对红血球进行过滤和分解，同时也是免疫系统的一部分，负责产生和储存淋巴细胞和抗体。常见的脾脏疾病包括脾梗死、脾功能亢进、脾肿大等。</p></div>
    <div v-show="shownum==='胆囊'"><p>胆囊是一个位于肝脏下方的小囊状器官，主要功能是储存由肝脏产生的胆汁，当身体需要时，胆囊会将胆汁释放到小肠中，帮助消化脂肪。常见的胆囊疾病包括胆囊结石、胆囊炎、胆囊切除术等。</p></div>
    <div v-show="shownum==='右肾'"><p>肾脏是人体内最重要的器官之一，主要功能是过滤血液，排除废物和过多的水分，并产生尿液。右肾和左肾位于腹腔内两侧，右肾比左肾略低，两者大小和功能相似。常见的肾脏疾病包括肾结石、肾囊肿、肾炎、肾衰竭等。</p></div>
    <div v-show="shownum==='左肾'"><p>肾脏是人体内最重要的器官之一，主要功能是过滤血液，排除废物和过多的水分，并产生尿液。右肾和左肾位于腹腔内两侧，右肾比左肾略低，两者大小和功能相似。常见的肾脏疾病包括肾结石、肾囊肿、肾炎、肾衰竭等。</p></div>
    <div v-show="shownum==='食管'"><p>食管是一条管状结构，连接口腔和胃，负责将食物运输到胃中。常见的食管疾病包括食管癌、食管炎、食管溃疡等。</p></div>
    <div v-show="shownum==='肝脏'"><p>肝脏是人体内最大的内脏器官之一，负责合成胆汁、代谢药物和毒素、储存能量等。常见的肝脏疾病包括肝炎、肝硬化、脂肪肝等。</p></div>
    <div v-show="shownum==='胃'"><p>胃是一个位于腹部的J形器官，主要功能是消化食物。常见的胃部疾病包括胃溃疡、胃癌、胃炎等。</p></div>
    <div v-show="shownum==='主动脉'"><p>主动脉和下腔动脉是人体内两条最大的血管，分别负责将氧和营养物质输送到全身组织和器官。常见的动脉疾病包括动脉硬化、动脉瘤、动脉闭塞等。</p></div>
    <div v-show="shownum==='下腔动脉'"><p>主动脉和下腔动脉是人体内两条最大的血管，分别负责将氧和营养物质输送到全身组织和器官。常见的动脉疾病包括动脉硬化、动脉瘤、动脉闭塞等。</p></div>
    <div v-show="shownum==='胰腺'"><p>胰腺是一个位于腹部的长形腺体，主要功能是产生胰液和激素，帮助消化食物和调节血糖水平。常见的胰腺疾病包括胰腺炎、胰腺癌等。</p></div>
    <div v-show="shownum==='右肾上腺'"><p>肾上腺是一对小腺体，位于肾脏上方，主要分泌肾上腺素和去甲肾上腺素，调节身体的代谢和应激反应。常见的肾上腺疾病包括肾上腺功能亢进症、肾上腺皮质功能减退症等。</p></div>
    <div v-show="shownum==='左肾上腺'"><p>肾上腺是一对小腺体，位于肾脏上方，主要分泌肾上腺素和去甲肾上腺素，调节身体的代谢和应激反应。常见的肾上腺疾病包括肾上腺功能亢进症、肾上腺皮质功能减退症等。</p></div>
    <div v-show="shownum==='十二指肠'"><p>十二指肠是一段位于胃和小肠之间的结肠，主要功能是将胆汁和胰液分泌到小肠中，帮助消化和吸收营养。常见的十二指肠疾病包括十二指肠溃疡、十二指肠癌等。</p></div>
    <div v-show="shownum==='膀胱'"><p>膀胱是一个储存尿液的器官，位于盆腔底部。常见的膀胱疾病包括膀胱炎、膀胱结石、膀胱癌等。膀胱的正常功能需要神经、肌肉和泌尿系统的协调工作。</p></div>
    <div v-show="shownum==='前列腺/子宫'"><p>前列腺是男性生殖系统的一部分，位于膀胱下方，主要分泌前列腺液，帮助维持精液的液态。常见的前列腺疾病包括前列腺炎、前列腺增生、前列腺癌等。子宫是女性生殖系统的一部分，位于盆腔内，主要功能是容纳和孕育胎儿。常见的子宫疾病包括子宫肌瘤、子宫内膜异位症、子宫癌等。子宫还参与了月经周期的调节和生殖激素的代谢。</p></div>
  </el-card>
  <change></change>
</template>


<script lang="ts" >
import axios from 'axios'
import type { TableColumnCtx } from 'element-plus'
import {ref}from 'vue'
import change from './change.vue'



export default{
  data()
  {
    return{
      certin:true,
      //tableData:[],
      shownum:'器官名称',
      tableData: []
    }
  },
  components:{
    change
  },
  methods:{
    handleclick()
    {
        axios.post("http://127.0.0.1:5000/analyse", 1).then(responce => {
          console.log(responce)
          this.tableData= responce.data
          console.log(this.tableData)
          this.certin=!this.certin
        })
    },
    editCurrentApplicationApproval(row){
      this.shownum=row.name
      console.log(this.shownum)
    },


  }
}










</script>

<style>
.button
{
  transform: translate(20vh,0);
}
.border
{
  background-color: mediumspringgreen;
  width: 60vw;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}


.box-card {
  width: 1200px;
}
</style>