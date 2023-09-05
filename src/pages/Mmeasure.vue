<template>
    <div class="measure-tool">
      <div class="ol-control"><button @click="measure('distence')">距</button></div>
      <div class="ol-control"><button @click="measure('area')">面</button></div>
      <div class="ol-control"><button @click="measure('angle')">角</button></div>
    </div>
  </template>
  
  <script>
  import { Draw } from "ol/interaction";
  import { Vector as VectorSource } from "ol/source";
  import { Vector as VectorLayer } from "ol/layer";
  import Overlay from 'ol/Overlay';
  import { Polygon, LineString } from 'ol/geom';
  import Feature from 'ol/Feature';
  import { unByKey } from 'ol/Observable'
  import { getLength, getArea } from 'ol/sphere';
  import Style from "ol/style/Style";
  import Stroke from "ol/style/Stroke";
  import Fill from "ol/style/Fill";
  import Circle from "ol/style/Circle";
  export default {
    props: ["map"],//地图组件传值
    data() {
      return {
        measureType: "diatence",
        draw: null,
        vectorLayer: null,
        tipDiv: null,
        pointermoveEvent: null, // 地图pointermove事件
        sketchFeature: null, // 绘制的要素
        geometryListener: null, // 要素几何change事件
        measureResult: "0" // 测量结果
      }
    },
    methods: {
      creatDraw(type) {
        let maxPoints = null;
        if (this.measureType == "angle") maxPoints = 3
        else maxPoints = null
  
        // 矢量图层源
        let vectorSource = new VectorSource({
          wrapX: false
        });
        // 矢量图层
        this.vectorLayer = new VectorLayer({
          source: vectorSource,
          style: new Style({
            fill: new Fill({
              color: 'rgba(252, 86, 49, 0.1)'
            }),
            stroke: new Stroke({
              color: '#fc5531',
              width: 3
            }),
            image: new Circle({
              radius: 0,
              fill: new Fill({
                color: '#fc5531'
              })
            })
          }),
          name: "测量图层"
        });
        this.map.addLayer(this.vectorLayer)
        this.draw = new Draw({
          source: vectorSource,
          type: type,
          maxPoints: maxPoints,
          style: new Style({
            fill: new Fill({
              color: 'rgba(252, 86, 49, 0.1)'
            }),
            stroke: new Stroke({
              color: '#fc5531',
              lineDash: [10, 10],
              width: 3
            }),
            image: new Circle({
              radius: 0,
              fill: new Fill({
                color: '#fc5531'
              })
            })
          }),
          // 绘制时点击处理事件
          condition: (evt) => {
            // 测距时添加点标注
            if (this.measureResult != "0" && !this.map.getOverlayById(this.measureResult) && this.measureType == "distence")
              this.creatMark(null, this.measureResult, this.measureResult).setPosition(evt.coordinate)
            return true
          }
        });
        this.map.addInteraction(this.draw);
  
        /**
         * 绘制开始事件
         */
        this.draw.on("drawstart", e => {
          this.sketchFeature = e.feature
          let proj = this.map.getView().getProjection()
          //******距离测量开始时*****//
          if (this.measureType == "distence") {
            this.creatMark(null, "起点", "start").setPosition(this.map.getCoordinateFromPixel(e.target.downPx_))
            this.tipDiv.innerHTML = "总长：0 m</br>单击确定地点，双击结束";
            this.geometryListener = this.sketchFeature.getGeometry().on('change', (evt) => {
              this.measureResult = this.distenceFormat(getLength(evt.target, { "projection": proj, "radius": 6378137 }))
              this.tipDiv.innerHTML = "总长：" + this.measureResult + "</br>单击确定地点，双击结束";
            })
          }
          //******面积测量开始时*****//
          else if (this.measureType == "area") {
            this.tipDiv.innerHTML = "面积：0 m<sup>2</sup></br>继续单击确定地点";
            this.geometryListener = this.sketchFeature.getGeometry().on('change', (evt) => {
              if (evt.target.getCoordinates()[0].length < 4) this.tipDiv.innerHTML = "面积：0m<sup>2</sup></br>继续单击确定地点";
              else {
                this.measureResult = this.formatArea(getArea(evt.target, { "projection": proj, "radius": 6378137 }))
                this.tipDiv.innerHTML = "面积：" + this.measureResult + "</br>单击确定地点，双击结束";
              }
            })
          }
          //******角度测量开始时*****//
          else if (this.measureType == "angle") {
            this.tipDiv.innerHTML = "继续单击确定顶点";
            this.geometryListener = this.sketchFeature.getGeometry().on('change', (evt) => {
              if (evt.target.getCoordinates().length < 3) this.tipDiv.innerHTML = "继续单击确定顶点";
              else {
                this.measureResult = this.formatAngle(evt.target)
                this.tipDiv.innerHTML = "角度：" + this.measureResult + "</br>继续单击结束";
              }
            })
          }
        });
  
        /**
         * 绘制开始事件
         */
        this.draw.on("drawend", e => {
          let closeBtn = document.createElement('span');
          closeBtn.innerHTML = "×";
          closeBtn.title = "清除测量"
          closeBtn.style = "width: 10px;height:10px;line-height: 12px;text-align: center;border-radius: 5px;display: inline-block;padding: 2px;color: rgb(255, 68, 0);border: 2px solid rgb(255, 68, 0);background-color: rgb(255, 255, 255);font-weight: 600;position: absolute;top: -25px;right: -2px;cursor: pointer;";
          closeBtn.addEventListener('click', () => {
            this.clearMeasure()
          })
          //******距离测量结束时*****//
          if (this.measureType == "distence") {
            this.creatMark(closeBtn, null, "close1").setPosition(e.feature.getGeometry().getLastCoordinate());
            this.creatMark(null, "总长：" + this.measureResult + "", "length").setPosition(e.feature.getGeometry().getLastCoordinate())
            this.map.removeOverlay(this.map.getOverlayById(this.measureResult))
          }
          //******面积测量结束时*****//
          else if (this.measureType == "area") {
            this.creatMark(closeBtn, null, "close2").setPosition(e.feature.getGeometry().getInteriorPoint().getCoordinates());
            this.creatMark(null, "总面积：" + this.measureResult + "", "area").setPosition(e.feature.getGeometry().getInteriorPoint().getCoordinates())
          }
          //******角度测量结束时*****//
          else if (this.measureType == "angle") {
            this.creatMark(closeBtn, null, "close3").setPosition(e.feature.getGeometry().getCoordinates()[1]);
            this.creatMark(null, "角度：" + this.measureResult + "", "angle").setPosition(e.feature.getGeometry().getCoordinates()[1])
          }
          // 停止测量
          this.stopMeasure();
        });
      },
      /**
       * 测量
       */
      measure(type) {
        if (this.draw != null) return false; // 防止在绘制过程再创建测量
        this.measureType = type;
        if (this.vectorLayer != null) this.clearMeasure();
        this.tipDiv = document.createElement('div');
        this.tipDiv.innerHTML = '单击确定起点';
        this.tipDiv.className = "tipDiv";
        this.tipDiv.style = "width:auto;height:auto;padding:4px;border:1px solid #fc5531;font-size:12px;background-color:#fff;position:relative;top:60%;left:60%;font-weight:600;"
  
        let overlay = new Overlay({
          element: this.tipDiv,
          autoPan: false,
          positioning: "bottom-center",
          id: "tipLay",
          stopEvent: false //停止事件传播到地图
        });
        this.map.addOverlay(overlay);
  
        this.pointermoveEvent = this.map.on("pointermove", evt => {
          overlay.setPosition(evt.coordinate)
        })
        if (this.measureType == "distence" || this.measureType == "angle") {
          this.creatDraw("LineString")
        }
        else if (this.measureType == "area") {
          this.creatDraw("Polygon")
        }
      },
      /**
       * 创建标记
       */
      creatMark(markDom, txt, idstr) {
        if (markDom == null) {
          markDom = document.createElement('div');
          markDom.innerHTML = txt
          markDom.style = "width:auto;height:auto;padding:4px;border:1px solid #fc5531;font-size:12px;background-color:#fff;position:relative;top:60%;left:60%;font-weight:600;"
        }
        let overlay = new Overlay({
          element: markDom,
          autoPan: false,
          positioning: "bottom-center",
          id: idstr,
          stopEvent: false
        });
        this.map.addOverlay(overlay)
        return overlay;
      },
      /**
       * 格式化距离结果输出
       */
      distenceFormat(length) {
        let output;
        if (length > 100) {
          output = (Math.round(length / 1000 * 100) / 100) + ' ' + 'km'; //换算成km单位
        } else {
          output = (Math.round(length * 100) / 100) + ' ' + 'm'; //m为单位
        }
        return output;//返回线的长度
      },
      /**
       * 格式化面积输出
       */
      formatArea(area) {
        let output;
        if (area > 10000) {
          output = (Math.round(area / 1000000 * 100) / 100) + ' ' + 'km<sup>2</sup>'; //换算成km单位
        } else {
          output = (Math.round(area * 100) / 100) + ' ' + 'm<sup>2</sup>';//m为单位
        }
        return output; //返回多边形的面积
      },
      /**
       * 计算角度输出
       */
      formatAngle(line) {
        var coordinates = line.getCoordinates();
        var angle = '0°';
        if (coordinates.length == 3) {
          const disa = getLength(new Feature({
            geometry: new LineString([coordinates[0], coordinates[1]])
          }).getGeometry(), {
            radius: 6378137,
            projection: this.map.getView().getProjection()
          });
  
          const disb = getLength(new Feature({
            geometry: new LineString([coordinates[1], coordinates[2]])
          }).getGeometry(), {
            radius: 6378137,
            projection: this.map.getView().getProjection()
          });
  
          const disc = getLength(new Feature({
            geometry: new LineString([coordinates[0], coordinates[2]])
          }).getGeometry(), {
            radius: 6378137,
            projection: this.map.getView().getProjection()
          });
          var cos = (disa * disa + disb * disb - disc * disc) / (2 * disa * disb); // 计算cos值
          angle = (Math.acos(cos) * 180) / Math.PI; // 角度值
          angle = angle.toFixed(2); // 结果保留两位小数
        }
        if (isNaN(angle)) return "0°"
        else return angle + "°"; // 返回角度
      },
      /**
       * 停止测量
       */
      stopMeasure() {
        this.tipDiv = null
        this.map.removeInteraction(this.draw); // 移除绘制组件
        this.draw = null;
        this.map.removeOverlay(this.map.getOverlayById("tipLay")) // 移除动态提示框
      },
      /**
       * 清除测量
       */
      clearMeasure() {
        this.vectorLayer.getSource().clear()
        this.map.getOverlays().clear()
        //移除监听事件
        unByKey(this.pointermoveEvent) // 清除鼠标在地图的pointermove事件
        unByKey(this.geometryListener) // 清除绘制图像change事件
        this.pointermoveEvent = null;
        this.geometryListener = null;
        this.measureResult = "0"
      }
    }
  }
  </script>
  
  <style scoped>
  .measure-tool {
    z-index: 1;
    position: absolute;
    left: 0.5em;
    top: 6em;
    width: 50px;
    height: 40px;
  }
  .measure-tool div:nth-child(2) {
    margin-top: 2em;
  }
  .measure-tool div:nth-child(3) {
    margin-top: 4em;
  }
  .measure-tool{
    width: 1000px;
    height: 1000px;
  }
  </style>
  