<template>
    <Menu></Menu>
    <el-main>
    <div id="app" @mousedown="handleMouseDown" @mousemove="handleMouseMove" @mouseup="handleMouseUp" @contextmenu.prevent>
        <canvas ref="canvas"></canvas>
    </div>
    

    </el-main>
</template>
<script>
import Menu from "./menu.vue"
export default ({
    components:{
        Menu,
    },
    data() {
        return {
        isDrawing: false,
        points: [],
        angle: null,
        };
    },
    mounted() {
    this.canvas = this.$refs.canvas;
    this.ctx = this.canvas.getContext("2d");
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  },
  methods: {
    handleMouseDown(e) {
    if (e.button === 0) {
        this.isDrawing = true;
        const rect = this.canvas.getBoundingClientRect();
        this.points.push({
        x: e.clientX - rect.left,
        y: e.clientY - rect.top,
        });
    }
    },
    handleMouseMove(e) {
  if (this.isDrawing) {
    const rect = this.canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    if (this.points.length === 1) {
      this.drawLine(this.points[0], { x, y });
    } else if (this.points.length === 2) {
      this.drawLine(this.points[0], this.points[1]);
      this.drawLine(this.points[1], { x, y });
      this.angle = this.calculateAngle(
        this.points[0],
        this.points[1],
        { x, y }
      );
      this.ctx.fillStyle = "black";
      this.ctx.font = "bold 12px Arial";
      this.ctx.fillText(`角度: ${this.angle}°`, this.points[1].x + 10, this.points[1].y + 10);
    }
  }
},
        handleMouseUp(e) {
        if (e.button === 0) {
            if (this.points.length === 2) {
            this.isDrawing = false;
            this.points = [];
            this.angle = null;
            }
        } else if (e.button === 2) {
            this.isDrawing = false;
            this.points = [];
            this.angle = null;
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        }
        },
        drawLine(start, end) {
        this.ctx.beginPath();
        this.ctx.moveTo(start.x, start.y);
        this.ctx.lineTo(end.x, end.y);
        this.ctx.stroke();
        },
        calculateAngle(p1, p2, p3) {
        const a = Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2);
        const b = Math.pow(p2.x - p3.x, 2) + Math.pow(p2.y - p3.y, 2);
        const c = Math.pow(p3.x - p1.x, 2) + Math.pow(p3.y - p1.y, 2);
        return Math.acos((a + b - c) / Math.sqrt(4 * a * b)) * (180 / Math.PI);
        },
    },
})
</script>

<style scoped>
.el-main{
    width: 86vw;
    height: 100vh;
    transform: translate(14vw,0);
    background-image: linear-gradient(45deg, #0778b0 0%, #e4efe9 100%);
}
</style>