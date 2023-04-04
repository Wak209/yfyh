<template>
    <br>
    <h2 style="color:mediumpurple;">&nbsp&nbsp&nbsp标签编辑并导出</h2>
    <br>
    <h3 style="color:mediumpurple;">选择标签</h3>
    <el-checkbox v-model="checked1" label="脾脏" size="small" />
    <el-checkbox v-model="checked2" label="右肾" size="small" />
    <el-checkbox v-model="checked3" label="左肾" size="small" />
    <el-checkbox v-model="checked4" label="胆囊" size="small" />
    <el-checkbox v-model="checked5" label="食管" size="small" />
    <el-checkbox v-model="checked6" label="肝脏" size="small" />
    <el-checkbox v-model="checked7" label="胃" size="small" />
    <el-checkbox v-model="checked8" label="主动脉" size="small" />
    <el-checkbox v-model="checked9" label="下腔动脉" size="small" />
    <el-checkbox v-model="checked10" label="胰腺" size="small" />
    <el-checkbox v-model="checked11" label="右肾上腺" size="small" />
    <el-checkbox v-model="checked12" label="左肾上腺" size="small" />
    <el-checkbox v-model="checked13" label="十二指肠" size="small" />
    <el-checkbox v-model="checked14" label="膀胱" size="small" />
    <el-checkbox v-model="checked15" label="前列腺/子宫" size="small" />
    <br><br>
    <el-button @click="handleClick">导出</el-button>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
const checked1 = ref(true)
const checked2 = ref(true)
const checked3 = ref(true)
const checked4 = ref(true)
const checked5 = ref(true)
const checked6 = ref(true)
const checked7 = ref(true)
const checked8 = ref(true)
const checked9 = ref(true)
const checked10 = ref(true)
const checked11 = ref(true)
const checked12 = ref(true)
const checked13 = ref(true)
const checked14 = ref(true)
const checked15 = ref(true)


const download = async() => {
        const fileUrl="/change.nii.gz"
        const response = await axios.get(`http://127.0.0.1:5000/download?file_url=${fileUrl}`, {
        responseType: 'blob'
    })
    saveAs(response.data, 'change.nii.gz')
}
function handleClick(){
    var list = [checked1,checked2,checked3,checked4,checked5,checked6,checked7,checked8,checked9,checked10,checked11,checked12,checked13,checked14,checked15]
    axios.post("http://127.0.0.1:5000/Change", list).then(responce => {
            download()
        })
}

</script>

