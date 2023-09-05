import { defineStore } from "pinia";
import { ref, reactive } from "vue";
import { Niivue } from "@niivue/niivue";
import { ElMessage } from "element-plus";

export const useTool = defineStore("tool", () => {
  // var
  var Views = ref();
  const volumes = ref([]);
  const toolSwitch = ref(false);
  const lastPos = reactive({ vox: "", str: "" });
  const choose = ref("Red");
  const pen = ref(false);
  const fill = ref(false);

  var Viewss = ref();
  const volumess = ref([]);

  function CanvasInit() {
    Views = new Niivue({
      logging: "true",
      dragAndDropEnabled: false,
      backColor: [255, 255, 255, 0],
      show3Dcrosshair: true,
      onLocationChange: handleIntensityChange,
    });

    Views.opts.multiplanarForceRender = true;
    Views.setRadiologicalConvention(false);
    Views.drawOpacity = 0.4;
    Views.setSliceMM(true);

    return Views;
  }
  function handleIntensityChange(data) {
    lastPos.vox = data.vox[0] + " , " + data.vox[1] + " , " + data.vox[2];
    let OriStr = data.string;
    let index = OriStr.indexOf("=");
    let str = OriStr.slice(index + 1);
    lastPos.str = str;
  }
  function handleTool(id, Pen, isFill) {
    toolSwitch.value = !toolSwitch.value;
    if (id) {
      choose.value = id;
    }
    if (Pen) {
      pen.value = Pen;
    }
    if (isFill) {
      fill.value = isFill;
    }
    handleColor();
  }
  function handleMouse(id,RulerColor) {
    console.log(id);
    switch (id) {
      
      case "none":
        Views.opts.dragMode = Views.dragModes.none;
        break;
      case "contrast":
        Views.opts.dragMode = Views.dragModes.contrast;
        break;
      case "measurement":
        Views.opts.rulerColor =RulerColor;
        Views.opts.dragMode = Views.dragModes.measurement;
        console.log(volumes)
        //Views.opts.rulerColor = [0.5, 0.5, 0.9, 0.3];
        break;
      case "pan":
        Views.opts.dragMode = Views.dragModes.pan;
        break;
      case "slicer":
        Views.opts.dragMode = Views.dragModes.slicer3D;
        break;
    }
  }

  function handleSave(id) {
    switch (id) {
      case "SaveDocument":
        Views.saveDocument("image.nvd");
        return;
      case "SaveImage":
        Views.saveImage("image.nii", true);
        return;
      case "SaveBitmap":
        Views.saveScene("image.png");
        return;
    }
  }
  function AddVolumesFile(file) {
    if (volumes.value.length == 0) {
      volumes.value.push(file);
      Attach();
    } else {
      RemoveVolumesFile();
      AddVolumesFile(file);
    }
  }
  function RemoveVolumesFile() {
    volumes.value.pop();
  }
  function setpen(key,color,fill){
   /* Views.setDrawingEnabled(true);
    Views.setPenValue(value, fill);*/
    if(key === true){
      Views.setDrawingEnabled(true);
      Views.setPenValue(color, fill);
    }
    else{
      Views.setDrawingEnabled(false);
    }
  }
  function Attach() {
    console.log(volumes)
    console.log(lastPos.str)
    const Views = CanvasInit();
    Views.attachTo("nv");
    let Volumes=volumes.value[0];
    console.log(Volumes)
    Views.loadVolumes([Volumes]);
    console.log(Volumes)
  }
  return {
    CanvasInit,
    handleIntensityChange,
    handleMouse,
    handleTool,
    handleSave,
    AddVolumesFile,
    RemoveVolumesFile,
    toolSwitch,
    lastPos,
    setpen,
  };
});
