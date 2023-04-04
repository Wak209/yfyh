<template>
    <NaV></NaV>
    <div class="link">
        <br><br>
        <span><h>飞桨ai studio：</h><a href="https://aistudio.baidu.com/aistudio/index">https://aistudio.baidu.com/aistudio/index</a></span>
        <br>
        <span><h>本网站基于baseline：</h><a href="https://aistudio.baidu.com/aistudio/projectdetail/5173243?contributionType=1&sUid=312316&shared=1&ts=1670244745572">https://aistudio.baidu.com/aistudio/projectdetail/5173243?contributionType=1&sUid=312316&shared=1&ts=1670244745572</a></span>
        <br>
        <span><h>数据集</h><a href="https://aistudio.baidu.com/aistudio/datasetdetail/179474">https://aistudio.baidu.com/aistudio/datasetdetail/179474</a></span>
    </div>
</template>

<script >
import { ref } from 'vue'
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
.link{
    width: 80%;
    transform: translate(10vw,0);
}
</style>