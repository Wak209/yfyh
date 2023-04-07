<template>

    <el-container>
    <el-header>
        <NaV></NaV>
    </el-header>
    <div class="backg">
    <el-main>
            <div class="first">
            <el-card  class="cardone" style="margin:auto; width: 65%;" >
                <div class="Img">
                    <img src="../assets/8.png" class="imgone"/>           
                    <img src="../assets/7.png" class="imgtwo"/>    
                </div>                             
                <div >
                    <span class="Titleone" style="font-size:larger ; font-weight:bold">3D医疗分割</span>
                    <div class="bottom">
                        <span class="introone">
                            &nbsp&nbsp&nbsp&nbsp本网页使用nnunet模型，可以对多种格式的腹部医学图像实现高精度分割任务。
                        </span>
                    </div>
                </div>
            </el-card>
            </div>
            
            <div class="two">
            <el-card  class="cardtwo" style="margin:auto; width: 65%;" >
                <div class="Img2">
                    <img src="../assets/10.png" class="imgthree"/>           
                    <img src="../assets/11.png" class="imgfour"/>  
                </div>                             
                <div >
                    <span class="Titletwo" style="font-size:larger ; font-weight:bold">视图工具</span>
                    <div class="bottom">
                        <span class="introtwo">
                            &nbsp&nbsp&nbsp&nbsp本网页有画笔、测量等工具，供您选择。
                        </span>
                    </div>
                </div>
            </el-card>
            </div>


            <div class="three">
            <el-card  class="cardthree" style="margin:auto; width: 65%;" >
                <div class="Img3">
                    <img src="../assets/12.png" class="imgfive"/>           
                </div>                             
                <div >
                    <span class="Titlethree" style="font-size:larger ; font-weight:bold">分析功能</span>
                    <div class="bottom">
                        <span class="introthree">
                            &nbsp&nbsp&nbsp&nbsp本网页可以根据推理结果分析得到各器官的直径、横截面、体积等数据，并通过现有的小型数据集分析得到健康程度。
                        </span>
                    </div>
                </div>
            </el-card>
            </div>
    </el-main></div>
    </el-container>
</template>

<script>
import NaV from "./Home.vue";

export default {
    data() {
        return {
        
        }
    },
    components:{
        NaV
    }

}
</script>

<style>
@import './/hue.css';

.first{
    position:absolute;
    top:20vh;
    display: table;
}
.Img{
    background-color:rgb(4, 71, 197);
}
.imgone{
    transform: translate(6vw,0);
}
.imgtwo{
    transform: translate(6vw,0);
}
.Titleone{
    font-family:"楷体";
}
.introone{
    font-family:"楷体";
}
.two{
    position:absolute;
    top:80vh;
    display: table;
}
.Img2{
    background-color:rgb(191, 4, 197);
}
.imgthree{
    transform: translate(6vw,0);
}
.imgfour{
    transform: translate(6vw,0);
}
.Titletwo{
    font-family:"楷体";
}
.introtwo{
    font-family:"楷体";
}
.three{
    width: 100%;
    position:absolute;
    top:150vh;
    display: table;
}
.Img3{
    background-color:rgb(36, 197, 4);
}
.imgfive{
    transform: translate(6vw,0);
}
.Titlethree{
    font-family:"楷体";
}
.introthree{
    font-family:"楷体";
}
</style>