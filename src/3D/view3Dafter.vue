<template>
  <div class="content">
    <div class="Canv">
      <canvas id="nv"></canvas>
    </div>
    <div class="port">
      <div class="pos">
        <article>坐标：[{{ lastPos.vox || "x ,y ,z" }}]</article>
      </div>
    </div>
  </div>
  <tool v-show="toolSwitch"></tool>
</template>
<script setup>
import { storeToRefs } from "pinia";
import { Niivue } from "@niivue/niivue";
import { reactive, onMounted } from "vue";
// fix path from loaction

const volumess = reactive({ url: "/after.nii.gz" });


// use Store



// attach to canvas
function canvasinit() {
    Viewss = new Niivue({
      logging: "true",
      dragAndDropEnabled: false,
      backColor: [255, 255, 255, 0],
      show3Dcrosshair: true,
      onLocationChange: handleIntensityChange2,
    })
    Viewss.opts.multiplanarForceRender = true;
    Viewss.setRadiologicalConvention(false);
    Viewss.drawOpacity = 0.4;
    Viewss.setSliceMM(true);
    return Viewss;
}

function Attach() {
  const Viewss = canvasinit();
  Viewss.attachTo("nv");
  let index = volumess.url.indexOf(".");
  console.log(volumess.url)
  let str = volumess.url.slice(index);
  if (str === ".nvd") {
    Viewss.loadDocumentFromUrl([volumess.url]);
  } else {
    Viewss.loadVolumes([volumess]);
  }
}

onMounted(() => {
  Attach();
});


</script>

<style lang="less" scoped>
.content {
  z-index: 1;
  height: 100vh;
  width: 100%;
  clear: both;
  .Canv {
    width: 100%;
    height: 80vh;
  }
  .port {
    width: 50%;
    height: 10vh;
    background-color: rgb(255, 255, 255);
    .pos {
      display: flex;
      flex-direction: column;
      justify-content: center;
      width: 20vw;
      height: 10vh;
      article {
        margin-left: 2vw;
        font-size: 1.4em;
        font-weight: 700;
        color: rgb(0, 0, 0);
      }
    }
  }
}
</style>
