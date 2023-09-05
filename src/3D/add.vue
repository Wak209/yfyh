<template>
    <el-upload
            class="buttonnn"
            :on-change="handleChange"
            multiple
            :auto-upload="false"
            :limit="1"
        >
            <el-button type="primary" class="finn">选择文件</el-button>
        </el-upload>
</template>


<script>
import axios from 'axios';
import { useTool } from '../store/index.js'
const Tool = useTool();
const {
  AddVolumesFile
} = Tool;
function    changevolumes(filename)
        {
            AddVolumesFile({url: "/vol/"+filename})
        }
export default{
    data(){
        return{
            fileList:[],
        }
    },
    methods:{
    changevolumes(filename)
        {
            AddVolumesFile({url: "/vol/"+filename})
        },
    handleChange(file, fileList)
        {
            
            this.fileList = fileList;
            console.log(this.fileList)
            var param = new FormData();
            
                            this.fileList.forEach(
                                (val, index) => {
                                    param.append("file", val.raw);
                                    console.log(val.raw)
                                }
                            );
                
                            axios.post("http://127.0.0.1:5000/uploadvol", param).then(responce => {
                    console.log(responce.data)
                    changevolumes(responce.data)
                });
        },
   
    }
}
</script>

<style scoped>
.finn{
    transform: translate(15vw,-3vh);
}
</style>