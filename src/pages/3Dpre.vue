<template>
  <div class="common-layout">
    <el-container>
      <el-header><NaV></NaV></el-header>
    <el-container>

    <el-main style="overflow:hidden" id="rightsrcoll">
      <el-row class="tac" :gutter="50" >
        <el-col :span="4" class="rightt">

        <div class="Right">
        <br>
        <h1 class="mb-2" style="color: cornflowerblue; font-size: large;">3D Segmentation</h1>
        <br>
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"

          style="height: 100%"
        >
          <el-menu-item index="1">
            <span>Navigator One</span>
          </el-menu-item>
          <el-menu-item index="2">
            <span>Navigator Two</span>
          </el-menu-item>
          <el-menu-item index="3" >
            <span>Navigator Three</span>
          </el-menu-item>
          <el-menu-item index="4">
            <span>Navigator Four</span>
          </el-menu-item>
        </el-menu>
        </div>
        </el-col>
          <el-col :span="20">
            <p><span  style="font-size:xx-large;  font-weight:bold ; color: cornflowerblue;" >1.上传文件&nbsp&nbsp&nbsp</span><span style="font-size:large;  font-weight:bold;color: cornflowerblue;" >(支持格式：nii、nii.gz、dcm、raw、mhd等)</span></p>
            <div class="upload">
            <div class="uploadbox">
              <el-upload
                class="upload-demo"
                drag
                :multiple="false"
                :limit="1"
                :auto-upload="false"
                action="none"
              >
                <el-icon class="el-icon--upload"><Plus /></el-icon>
                <div class="el-upload__text">拖拽文件或者<em>点击上传</em></div>
              </el-upload>
                <el-button
                  class="button1"
                  type="primary"
                  @click="HandleSubmit()"
                  style="text-align:center"
                >
                  确认上传
                </el-button>
            </div>
          </div>
          <ViewBefore></ViewBefore>
          <!--ViewThreed></ViewThreed-->


          <p><span  style="font-size:xx-large;  font-weight:bold; color: cornflowerblue;" >2.预测</span></p>
          <br><br>
          <div class = "con">
          <el-tooltip content="单个模型预测，预计3-5分钟" placement="bottom" effect="light">
            <el-button class="button2" type="primary"  :loading="ConfirmLoadinglow" @click ="ConfirmLow" round>预测</el-button>
          </el-tooltip>
          <el-tooltip content="采用5个模型融合预测，预计20-30分钟" placement="bottom" effect="light">
            <el-button  color="#626aef"  class="button3" type="primary"  :loading="ConfirmLoadinghigh" @click ="ConfirmHigh" round >高精度预测</el-button>
          </el-tooltip></div>
          <!--ViewThreedafter></ViewThreedafter-->
          <ViewThreed></ViewThreed>
          <div style="text-align: center;">
          <el-button  color="#626aef" type="primary"   round >下载</el-button> </div>



          <span  style="font-size:xx-large;  font-weight:bold; color: cornflowerblue;" >3.处理</span>
          <br><br>
          <el-tabs type="border-card" class="demo-tabs">
            <el-tab-pane>
              <template #label>
                <span class="custom-tabs-label">
                  <el-icon><setting /></el-icon>
                  <span>标签管理</span>
                </span>
              </template>
              Route
            </el-tab-pane>
            <el-tab-pane>
              <template #label>
                <span class="custom-tabs-label">
                  <el-icon><EditPen /></el-icon>
                  <span>画笔工具</span>
                </span>
              </template>
              Route
            </el-tab-pane>

            <el-tab-pane>
              <template #label>
                <span class="custom-tabs-label">
                  <span>橡皮擦工具</span>
                </span>
              </template>
              Route
            </el-tab-pane>

          </el-tabs>

          <br>
          <span  style="font-size:xx-large;  font-weight:bold; color: cornflowerblue;" >4.分析</span>
          



        </el-col>
      </el-row>
    </el-main>
    </el-container></el-container>
  </div>
</template>


<script lang="ts">

import { onMounted, ref } from "vue";
import { UploadFilled } from "@element-plus/icons-vue";
import { useRouter } from "vue-router";
import { useTool, useAside } from "../store/index";
import  NaV  from "./Home.vue";
import  Menu  from "./Nav.vue";
import  ViewThreed from"../3D/view3D.vue"
import  ViewThreedafter from "../3D/view3Dafter.vue"
import  ViewBefore from "../3D/viewbefore.vue"

const router = useRouter();
const Tool = useTool();
const Aside = useAside();
const { handlePreView } = Aside;
const { getVolumesFile, AddVolumesFile, RemoveVolumesFile } = Tool;
const activeIndex2 = ref('1')


export default{
  data(){
    return {
      //滚动条高度
      scroll: '',
      //当前显示的菜单区域
      istyle: -1,
      ConfirmLoadinglow:false,
      ConfirmLoadinghigh:false,
    }
  },
  components:{
    NaV,
    Menu,
    ViewThreed,
    ViewThreedafter,
    ViewBefore,
  },
  methods:{
    
    HandleSubmit() {
      const Volumes = getVolumesFile();
      //console.log(Volumes)
      //console.log(lastPos.str)
      if (Volumes.value.length) {
        //console.log('haha')
        //router.push("/preview");
        handlePreView();
      } else {
        //this.$router.push("/three/preview");
        handlePreView();
      }
    },
    handleOpen : (key: string, keyPath: string[]) => {
      console.log(key, keyPath)
    },
    handleClose : (key: string, keyPath: string[]) => {
      console.log(key, keyPath)
    },
    ConfirmLow(){
      this.ConfirmLoadinglow=true;
    },
    ConfirmHigh(){
      this.ConfirmLoadinghigh=true;
    },
  }
}




</script>

<style lang="less" scoped>
.rightt{
  
  position: fixed;
  .el-menu{
    height: 100%;
    position: fixed;
  }
}
  .upload {
  height: 45vh;
  width: 100%;
  .uploadbox {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    .upload-demo {
      background: rgb(236, 241, 241);
      border-radius: 25px;
      width: 30vw;
      height: 30vh;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      border-radius: 30px;
      :deep(.el-upload-dragger) {
        width: 15vw;
        height: 18vh;
        border: none;
        background: rgba(255, 255,255, 0);
        backdrop-filter: blur(8px);
        border-radius: 25px;
        box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
      }
      :deep(.el-upload-list__item, .is-ready) {
        transform: translate(0, -4vh);
        font-size: 24px;
        height: 4vh;
        line-height: 4vh;
        width: 10vw;
      }
      :deep(.el-upload-list__item, .is-ready):hover {
        background-color: #e4efe9;
      }
      .el-upload__text {
        font-size: 12px;
      }
    }
    .upload-demo:hover {
      border-color: #409eff;
    }
    .el-button {
      transform: translate(0vw, -7vh);
    }
  }
}
  
.con{ 
  height: 10vh;
  width: 100%;
  .button2{
    transform: translate(20vw,0vh);
  }
  .button3{
    transform: translate(40vw,0vh);
  }
}

.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
.demo-tabs .custom-tabs-label .el-icon {
  vertical-align: middle;
}
.demo-tabs .custom-tabs-label span {
  vertical-align: middle;
  margin-left: 4px;
}

</style>

