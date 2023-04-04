<template>
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
</template>

<script>
export default{
    methods:{
        HandleSubmit() {
            const Volumes = getVolumesFile();
            if (Volumes.value.length) {
                handlePreView();
            } 
            else {
                handlePreView();
            }
        }
    }
}
</script>

<style>
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
</style>