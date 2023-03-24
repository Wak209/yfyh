<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="auto">
        <side></side>
      </el-aside>
      <el-container>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>

    <el-backtop :bottom="30">
    <!--div style="{
      height: 100%;
      width: 100%;
      background-color: #f2f5f6;
      box-shadow: 0 0 6px rgba(0,0,0, .12);
      text-align: center;
      line-height: 40px;
      color: #1989fa;
      }"></div-->
  </el-backtop>

  </div>
</template>

<script >

</script>


