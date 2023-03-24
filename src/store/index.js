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


  // 初始化渲染器
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

  function canvasInit() {
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
  // 相关配置

  function handleIntensityChange(data) {
    lastPos.vox = data.vox[0] + " , " + data.vox[1] + " , " + data.vox[2];
    let OriStr = data.string;
    let index = OriStr.indexOf("=");
    let str = OriStr.slice(index + 1);
    lastPos.str = str;
  }

  // 工具栏开关
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
  // 鼠标右键工具
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
        Views.opts.dragMode = Views.dragModes.measurement;
        //Views.opts.rulerColor = [0.5, 0.5, 0.9, 0.3];
        Views.opts.rulerColor =RulerColor;
        break;
      case "pan":
        Views.opts.dragMode = Views.dragModes.pan;
        break;
      case "slicer":
        Views.opts.dragMode = Views.dragModes.slicer3D;
        break;
    }
  }
  // 视图工具
  function handleScreen(id) {
    switch (id) {
      case "Axial":
        Views.setSliceType(Views.sliceTypeAxial);
        break;
      case "Sagittal":
        Views.setSliceType(Views.sliceTypeSagittal);
        break;
      case "Coronal":
        Views.setSliceType(Views.sliceTypeCoronal);
        break;
      case "Render":
        Views.setSliceType(Views.sliceTypeRender);
        break;
      case "ACS":
        Views.opts.multiplanarForceRender = false;
        Views.setSliceType(Views.sliceTypeMultiplanar);
        break;
      case "ACSR":
        Views.opts.multiplanarForceRender = true;
        Views.setSliceType(Views.sliceTypeMultiplanar);
        break;
    }
  }
  // 画笔颜色工具
  function handleColor() {
    Views.setDrawingEnabled(pen.value);
    switch (choose.value) {
      case "Red":
        Views.setPenValue(1, fill.value);
        break;
      case "Green":
        Views.setPenValue(2, fill.value);
        break;
      case "Blue":
        Views.setPenValue(3, fill).value;
        break;
      case "Yellow":
        Views.setPenValue(4, fill.value);
        break;
      case "Cyan":
        Views.setPenValue(5, fill);
        break;
      case "Purple":
        Views.setPenValue(6, fill);
        break;
      case "Erase":
        Views.setPenValue(0, fill);
        break;
    }
  }
  function HandleColor(color) {
    Views.setDrawingEnabled(pen.value);
    switch (color) {
      case "Red":
        Views.setPenValue(1, fill.value);
        break;
      case "Green":
        Views.setPenValue(2, fill.value);
        break;
      case "Blue":
        Views.setPenValue(3, fill).value;
        break;
      case "Yellow":
        Views.setPenValue(4, fill.value);
        break;
      case "Cyan":
        Views.setPenValue(5, fill);
        break;
      case "Purple":
        Views.setPenValue(6, fill);
        break;
      case "Erase":
        Views.setPenValue(0, fill);
        break;
    }
  }
  // 保存相关工具
  function handleSave(id) {
    switch (id) {
      case "SaveDocument":
        Views.saveDocument("all.nvd");
        return;
      case "SaveImage":
        Views.saveImage("all.nii", true);
        return;
      case "SaveBitmap":
        Views.saveScene("ScreenShot.png");
        return;
    }
  }
  // 更改材质
  function handleMaterial(index, id) {
    Views.volumes[index].colorMap = id;
    Views.updateGLVolume();
    return;
  }
  // 添加文件时的相关操作
  function AddVolumesFile(file) {
    if (volumes.value.length == 0) {
      volumes.value.push(file);
    } else {
      ElMessage({
        showClose: true,
        message: "仅限单个文件上传",
        type: "warning",
      });
    }
  }
  function RemoveVolumesFile() {
    volumes.value.pop();
  }
  function getVolumesFile() {
    return volumes;
  }
  // 拿到渲染器
  function getViews() {
    return Views;
  }
  return {
    CanvasInit,
    canvasInit,
    handleIntensityChange,
    handleColor,
    handleScreen,
    handleMouse,
    handleTool,
    handleSave,
    handleMaterial,
    getVolumesFile,
    getViews,
    AddVolumesFile,
    RemoveVolumesFile,
    toolSwitch,
    lastPos,
    HandleColor
  };
});
export const useAside = defineStore("user", () => {
  var isUpload = ref(true);
  function handlePreView() {
    isUpload.value = !isUpload.value;
  }
  return {
    handlePreView,
    isUpload,
  };
});
