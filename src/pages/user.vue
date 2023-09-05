<template>
    <Menu></Menu>
    <el-main>
      <el-row>
        <el-col :span="10">
          <el-icon :size="40" style="width:50px; height: 50px; position: relative; left:5%; top:50%"><UserFilled /></el-icon>
          <h1 style="font-size:30px; position: relative ;left: 15%;" >用户{{phonenum}}，您好！</h1>
        </el-col>
        <el-col :span="3">
          <div class="statistic-card" style="position: relative;  top:18%">
          <el-statistic :value="11">
            <template #title>
              <div style="display: inline-flex; align-items: center">
                总使用次数
                <el-tooltip
                  effect="dark"
                  content="使用本网页推理总次数"
                  placement="top"
                >
                  <el-icon style="margin-left: 4px" :size="12">
                    <Warning />
                  </el-icon>
                </el-tooltip>
              </div>
            </template>
          </el-statistic>
          <!--div class="statistic-footer">
            <div class="footer-item">
              <span>month on month</span>
              <span class="red">
                12%
                <el-icon>
                  <CaretBottom />
                </el-icon>
              </span>
            </div>
          </div-->
        </div>
        </el-col>
        <el-col :span="3">
          <div class="statistic-card" style="position: relative;  top:18%">
          <el-statistic :value="11">
            <template #title>
              <div style="display: inline-flex; align-items: center">
                今日使用次数
                <el-tooltip
                  effect="dark"
                  content="今天使用本网页推理总次数"
                  placement="top"
                >
                  <el-icon style="margin-left: 4px" :size="12">
                    <Warning />
                  </el-icon>
                </el-tooltip>
              </div>
            </template>
          </el-statistic>
          <div class="statistic-footer">
            <div class="footer-item">
              <span style="font-size: 10px">较昨天</span>
              <span class="red">
                1
                <el-icon>
                  <CaretTop />
                </el-icon>
              </span>
            </div>
          </div>
        </div>
        </el-col>
      </el-row>
    <el-divider  content-position="center" color="black" class="divider"></el-divider>
    <el-row :gutter="10" class="row-divider" >
      <el-col :span="8" class="col-divider">
        <h1>上传文件：</h1>
        <li v-for="before_folder in before_folders " :key="before_folder.id">
          <a class="hover-image" href="#" @click="downloadBefore(before_folder.name,$event)" @mouseover="beforeshowImg($event)">
            {{ before_folder.name }}
            <span class="image-popup"><img class="afterimg" width="200" height="200"></span>
            <!--span class="image-popup"><img src="../../public/15972129987/before/1.jpg" width="200" height="200"></span-->
          </a>
        </li>
      </el-col>
      <el-col :span="8" class="col-divider">
        <h1>分割结果：</h1>
        <li v-for="after_folder in after_folders " :key="after_folder.id">
          <a  href="#" @click="downloadAfter(after_folder.name,$event)" >
            {{ after_folder.name }}
            <!--span class="image-popup"><img src="../../public/15972129987/before/1.jpg" width="200" height="200"></span-->
          </a>
        </li>
      </el-col>
      <el-col :span="8" >
        <h1>统计图片：</h1>
        <li v-for="graph_folder in graph_folders " :key="graph_folder.id">
          <a class="hover-image" href="#" @click="downloadGraph(graph_folder.name,$event)" @mouseover="showImg($event)">
            {{ graph_folder.name }}
            <span class="image-popup"><img class="graphimg" width="200" height="200"></span>
          </a>
        </li>
      </el-col>
    </el-row>
    </el-main>
</template>
<script>
import Menu from "./menu.vue"
import axios from "axios";
import { saveAs } from 'file-saver';

export default ({
  components:{
    Menu,
  },
  mounted(){
    this.fetchFolders();
  },
  data()
  {
    return{
      phonenum:15972129987,
      before_folders: [],
      after_folders: [],
      graph_folders: [],
    }
  },
  methods: {
    fetchFolders(){
      axios.post("http://127.0.0.1:5000/folders", "1").then(responce => {
        console.log(responce.data)
        this.before_folders = responce.data.map((name, index) => ({ id: index, name }));
        console.log(this.before_folders)
    });
      axios.post("http://127.0.0.1:5000/afterfolders", "1").then(responce => {
        console.log(responce.data)
        this.after_folders = responce.data.map((name, index) => ({ id: index, name }));
        console.log(this.after_folders)
    });
      axios.post("http://127.0.0.1:5000/graphfolders", "1").then(responce => {
        console.log(responce.data)
        this.graph_folders = responce.data.map((name, index) => ({ id: index, name }));
        console.log(this.graph_folders)
    });
    },
    
    async downloadBefore(filename,event) {
      event.preventDefault();
      this.fileUrl="public\\15972129987\\before\\"+filename.toString()
      const response = await axios.get(`http://127.0.0.1:5000/download?file_url=${this.fileUrl}`, {
        responseType: 'blob'
      })
      saveAs(response.data, filename.toString())

    },
    async downloadAfter(filename,event) {
      event.preventDefault();
      this.fileUrl="public\\15972129987\\after\\"+filename.toString()
      const response = await axios.get(`http://127.0.0.1:5000/download?file_url=${this.fileUrl}`, {
        responseType: 'blob'
      })
      saveAs(response.data, filename.toString())

    },
    async downloadGraph(filename,event) {
      event.preventDefault();
      this.fileUrl="public\\15972129987\\graph\\"+filename.toString()
      const response = await axios.get(`http://127.0.0.1:5000/download?file_url=${this.fileUrl}`, {
        responseType: 'blob'
      })
      saveAs(response.data, filename.toString())

    },
    showImg: function(event){
      var graphName = event.target.textContent.trim();
      var imageUrl = "../../public/15972129987/graph/"+graphName+"?v="+ new Date().getTime(); 
      console.log(imageUrl)
      event.target.querySelector(".graphimg") .src = imageUrl;
    },
    beforeshowImg: function(event){
      var graphName = event.target.textContent.trim();
      var imageUrl = ""
      //<!--span class="image-popup"><img src="../../public/15972129987/before/1.jpg" width="200" height="200"></span-->
      //var imageUrl = "../../public/15972129987/before/"+graphName+"?v="+ new Date().getTime(); 
      if (graphName === "20230602_0000.nii.gz"){
        imageUrl = "../../public/15972129987/before/0602_1.jpg"+"?v="+ new Date().getTime(); 
      }
      else if (graphName === "20230711_0000.nii.gz"){
        imageUrl = "../../public/15972129987/before/0711_1.jpg"+"?v="+ new Date().getTime(); 
      }
      else{
        imageUrl = "../../public/15972129987/before/1.jpg"+"?v="+ new Date().getTime();
      }
      console.log(imageUrl)
      event.target.querySelector(".afterimg") .src = imageUrl;
    }
  }
})
</script>

<style scoped>
.el-main{
    width: 86vw;
    height: 100vh;
    transform: translate(14vw,0);
    background-image: linear-gradient(45deg, #e7f49f 0%, #e4efe9 100%);
}
.demo-type {
  display: flex;
}
.demo-type > div {
  flex: 1;
  text-align: center;
}
.divider{
  border-width:4px ;
  border-color: black;
}

.row-divider {
  display: flex;
  flex-direction: row;
  width: 100%;
}
.col-divider {
  height: 770px;
  border-right: 1px solid black;
}
a.hover-image {
  position: relative;
}

a.hover-image .image-popup {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
}

a.hover-image:hover .image-popup {
  display: block;
}

</style>