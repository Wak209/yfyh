<template>
    <!--br>
    <h2 style="color:mediumpurple;">&nbsp&nbsp&nbsp多文件分析、筛选</h2>
    <br-->
    <div>
        <el-upload
            :file-list="fileList"
            class="upload-demo inline-block"
            :multiple="false"
            :auto-upload="false"
            :on-remove="fileRemove"
            :limit="10"
            :on-change="handleFileChanged"
        >
            <el-button type="primary">选择文件</el-button>
        </el-upload>
        <el-select v-model="value" class="select inline-block" placeholder="Select" @change="haddleselectchange">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"        
            />
        </el-select>
        <el-button class="ml-3 inline-block" type="success" @click="submitUpload" :loading="load">分析</el-button>
    </div>
    <el-table
    class="Table"
    :data="tableData"
    :key="certin"
    style="width: 82%"
    @row-click="editCurrentApplicationApproval"
    >
    <el-table-column prop="name" label="文件名"  width="200" />
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
  <img v-show="isshowed" src="../../public/15972129987/graph/compare1.jpg?v=1" id="Image" class="pic1"/>
</template>

<script>
import { method } from 'lodash';
import axios from 'axios';


export default {
    data(){
        return {
            load:false,
            fileList:[],
            value : 0,
            tableData:[],
            tableList:[],
            certin:true,
            isshowed:false,
            Options :[
            {
                value: 0,
                label: '脾脏',
            },
            {
                value: 1,
                label: '右肾',
            },
            {
                value: 2,
                label: '左肾',
            },
            {
                value: 3,
                label: '胆囊',
            },
            {
                value: 4,
                label: '食管',
            },
            {
                value: 5,
                label: '肝脏',
            },
            {
                value: 6,
                label: '胃',
            },
            {
                value: 7,
                label: '主动脉',
            },
            {
                value: 8,
                label: '下腔动脉',
            },
            {
                value: 9,
                label: '胰腺',
            },
            {
                value: 10,
                label: '右肾上腺',
            },
            {
                value: 11,
                label: '左肾上腺',
            },
            {
                value: 12,
                label: '十二指肠',
            },
            {
                value: 13,
                label: '膀胱',
            },
            {
                value: 14,
                label: '前列腺/子宫',
            },
            ],
            options :[
            {
                value: 0,
                label: '脾脏',
            },
            {
                value: 1,
                label: '右肾',
            },
            {
                value: 2,
                label: '左肾',
            },
            {
                value: 3,
                label: '胆囊',
            },
            {
                value: 4,
                label: '食管',
            },
            {
                value: 5,
                label: '肝脏',
            },
            {
                value: 6,
                label: '胃',
            },
            {
                value: 7,
                label: '主动脉',
            },
            {
                value: 8,
                label: '下腔动脉',
            },
            {
                value: 9,
                label: '胰腺',
            },
            {
                value: 13,
                label: '膀胱',
            },
            ],
        }
    },
    methods:{
        handleFileChanged (file, fileList)  { 
                // 检查是否有重复文件，有的话删除新选择的文件     
                if(fileList.findIndex(f=>f.name===file.name)!=fileList.findLastIndex(f=>f.name===file.name))
                {
                    ElMessage.info(file.name +" 文件已存在")
                    fileList.pop()
                }
                this.fileList = fileList
                console.log(this.fileList)
        },
        fileRemove(file, fileList) {
            this.fileList = fileList
        },
        submitUpload(){
            this.load=true
            var param = new FormData();
            this.fileList.forEach(
						(val, index) => {
							param.append("file", val.raw);
						}
					);
            axios.post("http://127.0.0.1:5000/uploadall", param).then(responce => {
                this.load=false
                this.tableList= responce.data
                this.isshowed=true
                var image = document.getElementById("Image");
                image.src = "../../public/15972129987/graph/compare1.jpg?v=" + new Date().getTime();
                console.log(this.tableList)
                this.tableData = this.tableList[0]
                this.certin=!this.certin
                });
        },
        haddleselectchange(val)
        {
            console.log(this.isshowed)
            console.log(val)
            //console.log(value)
            this.tableData = this.tableList[val]
            var image = document.getElementById("Image");
            image.src = "../../public/15972129987/graph/compare"+(this.value+1).toString()+".jpg?v=" + new Date().getTime();
            this.certin=!this.certin
        }
    }
}
</script>

<style scoped>
.upload-demo{
    width: 20%;
    transform: translate(10vw,0);
}
.ml-3{
    transform: translate(-2vw,0);
}
.select{
    transform: translate(28vw,0);
}
.inline-block {
  display: inline-block;
}
.pic1{
    position: relative;
    left: 20%;
}
</style>

