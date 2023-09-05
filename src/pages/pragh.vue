<template>
    <Menu></Menu>
    <el-main>
        <el-tabs v-model="activeName" class="my-tabs" >
            <el-tab-pane label="上传文件数据分析" name="first" >
                <show></show>
            </el-tab-pane>
            <el-tab-pane label="上传文件对比分析" name="second">
                <compare></compare>
            </el-tab-pane>
        </el-tabs>
    </el-main>

</template>
<script>
import Menu from "./menu.vue"
import { onMounted, ref } from "vue";
import show from "../3D/analysis.vue"
import compare from "../3D/userdecide.vue"
export default ({
    components:{
        Menu,
        show,
        compare,
    },
    data() {
        return {
            activeName:'first',
        }
    },
    methods: {
    }
})
</script>
<style scoped>
.el-main{
    width: 86vw;
    height: 100vh;
    padding: 0;
    top: 0;
    transform: translate(14vw,0);
    background-image: linear-gradient(45deg, #07a7af 0%, #e4efe9 100%);
}
.my-tabs
{
    margin: 10px 20px;

}
.my-tabs>>> .el-tabs__item{
    font-size: 18px ;
    font-family:'Times New Roman', Times, serif;
    font-weight: 1000;
}
.my-tabs>>> .el-tabs__nav-wrap::after{
    width: 76%;
}
</style>