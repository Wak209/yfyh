<template>
    <div class="common-layout">
        <el-container class="Tou " style="overflow:hidden" >
        <el-header><NaV></NaV></el-header>
        <el-container >
          
            <el-aside >
                <br>
                <h1 class="mb-2" style="color: cornflowerblue; font-size: large;">3D Segmentation</h1>
                <br>
                <el-menu
                :default-active="active"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
                >
                <el-menu-item index="1" @click="clicknav(1)" name ='tab0'>
                  <span>Navigator One</span>
                </el-menu-item>
                
                <el-menu-item index="2" @click="clicknav(2)" name ='tab1'>
                  <span>  Navigator two </span>
                </el-menu-item>

                <el-menu-item index="3" @click="clicknav(3)" name ='tab2'>
                  <span>Navigator Three</span>
                </el-menu-item>

                <el-menu-item index="4" @click="clicknav(4)" name ='tab3'>
                 <span>Navigator Four</span>

                </el-menu-item>
                </el-menu>
            </el-aside>
          
          
              <el-main >
             
                <p><span  style="font-size:xx-large;  font-weight:bold ; color: cornflowerblue;" id ="one" class="section">1.上传文件&nbsp&nbsp&nbsp</span><span style="font-size:large;  font-weight:bold;color: cornflowerblue;" >(支持格式：nii、nii.gz、dcm、raw、mhd等)</span></p>

                <div class="Conv">
                    <canvas id="gl"></canvas>
                </div>
                <!--ViewBefore></ViewBefore-->

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
                <!--ViewBefore></ViewBefore-->
                <!--ViewThreed></ViewThreed-->


                <p><span  style="font-size:xx-large;  font-weight:bold; color: cornflowerblue;"  id ="two" class="section">2.预测</span></p>
                <br><br>
                <div class = "con">
                <el-switch
                  v-model="value1"
                  class="switch1"
                  @change="switchChange"
                  active-text="高精度"
                  inactive-text="正常"/>
                <el-tooltip content="单个模型预测，预计3-5分钟" placement="bottom" effect="light">
                    <el-button class="button2" type="primary"  :loading="ConfirmLoadinglow" @click ="ConfirmLow" round>预测</el-button>
                </el-tooltip>
                <!--el-tooltip content="采用5个模型融合预测，预计20-30分钟" placement="bottom" effect="light">
                    <el-button  color="#626aef"  class="button3" type="primary"  :loading="ConfirmLoadinghigh" @click ="ConfirmHigh" round >高精度预测</el-button>
                </el-tooltip--></div>
                <!--ViewThreedafter></ViewThreedafter-->
                <ViewThreed></ViewThreed>
                <el-button  color="#626aef" type="primary"   round class="download-button" @click="testt">导出</el-button> 



                <p><span  style="font-size:xx-large;  font-weight:bold; color: cornflowerblue;"  id ="three" class="section">3.视图</span></p>
                <br><br>
                <tool></tool>

                <span  style="font-size:xx-large;  font-weight:bold; color: cornflowerblue;"   id ="four" class="section">4.分析</span>




              
              </el-main>
        </el-container>
        </el-container>
    </div>

</template>

<script>

import { onMounted, ref } from "vue";
import { UploadFilled } from "@element-plus/icons-vue";
import { useRouter } from "vue-router";
import { useTool, useAside } from "../store/index";
import  NaV  from "./Home.vue";
import  Menu  from "./Nav.vue";
import  ViewThreed from"../3D/view3D.vue"
import  ViewThreedafter from "../3D/view3Dafter.vue"
import  ViewBefore from "../3D/viewbefore.vue"
import {Niivue} from '@niivue/niivue'
import tool from '../3D/3Dtool.vue'

const nv = new Niivue()


const router = useRouter();
const Tool = useTool();
const Aside = useAside();
const { handlePreView } = Aside;
const { getVolumesFile, AddVolumesFile, RemoveVolumesFile } = Tool;
const activeIndex2 = ref('1')


export default{
  data(){
    return {
      activeName:'tab1',
      scroll:'',
      istyle:-1,
      active:"1",
      ConfirmLoadinglow:false,
      ConfirmLoadinghigh:false,
      volumeList: [
        {
          url: "/before.nii.gz",
        },
      ]
    }
  },
  components:{
    NaV,
    Menu,
    ViewThreed,
    ViewThreedafter,
    ViewBefore,
    tool,
  },

  mounted(){
    window.addEventListener('scroll', this.dataScroll);
    nv.attachTo('gl');
    nv.loadVolumes(this.volumeList);
  },
  destroy() {
    // 必须移除监听器，不然当该vue组件被销毁了，监听器还在就会出错
    window.removeEventListener('scroll', this.onScroll)
  },
  methods:{
    dataScroll: function () {
        this.scroll = document.documentElement.scrollTop || document.body.scrollTop;
      },
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

    ConfirmLow(){
      this.ConfirmLoadinglow=true;
    },
    ConfirmHigh(){
      this.ConfirmLoadinghigh=true;
    },
    testt(tab){
      window,scrollTo(0,0);
      console.log(tab);
    },
    clicknav(tab){
        console.log(tab)
        this.jump(tab)
    },
    jump(index) {
        let jump = document.getElementsByClassName('section');
        // 获取需要滚动的距离
        let total = jump[index-1].offsetTop;
        // Chrome
        document.body.scrollTop = total;
        // Firefox
        document.documentElement.scrollTop = total;
        // Safari
        window.pageYOffset = total;
        // $('html, body').animate({
        // 'scrollTop': total
        // }, 400);
    },
    loadScroll: function () {
        var self = this;
        var sections = document.getElementsByClassName('section');
        for (var i = sections.length - 1; i >= 0; i--) {
          if (self.scroll >= sections[i].offsetTop - 100) {
          //我在上面规定了每个el-tab-pane标签的name属性值为tab+该标签的index值
            self.active=i+1;
            self.activeName = 'tab'+i;
            //console.log(self.activeName);
            break;
          }
        }
      },
  },
  watch: {
    //监听scroll变量，只要滚动条位置变化就会执行方法loadScroll
      scroll: function () {
        this.loadScroll()
      }
    },

}




</script>
<style lang="less" scoped>
.el-header{
  width: 70 vw;
}
.el-aside{
  width: 10vw;
  height: 100%;
  position: fixed;
}
.el-main{
  .el-menu-item {
    background-color: rgba(255, 255, 255, 1);
  }
  .el-menu-item.is-active {
    background-color: #40e669 !important;
  }
  width: 88vw;
  height: 100%;

  position: relative;
  left:10vw;

  .upload {
    height: 45vh;
    width: 80vw;
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
  .switch1{
        transform: translate(15vw,0vh);
  }
  .conv{
      width: 80vw;
  
    }
  .con{ 
    height: 5vh;
    width: 80vw;
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
  .download-button{
    position: relative;
    transform: translate(40vw,0vh);
  }
  .el-tabs{
    width: 80vw;
  }
}

</style>
