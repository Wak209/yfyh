<template>
  <el-aside>
      <!--h1 class="mb-2"  style="color: rgb(23, 241, 165); font-size: x-large;">医分译毫</h1>
      <br-->
      <img src="../assets/logo.png" class="logo" width="70" height="70"/>
      <h1 class="mb-2"  style="color: rgb(59, 240, 234); font-size: x-large;">医分译毫</h1>
			<!--el-menu        class=el-menu-vertical-demo" 
      >
				<el-menu-item index="1" class="tab1" >
          <span style="color:white">Navigator One</span>
        </el-menu-item>
        <el-menu-item index="2" class="tab2">
          <span style="color:white">Navigator Two</span>
        </el-menu-item>
        <el-menu-item index="3" class="tab3">
          <span style="color:white">Navigator Three</span>
        </el-menu-item>
        <el-menu-item index="4" class="tab4">
          <span style="color:white">Navigator Four</span>
        </el-menu-item>
      </el-menu-->
	<el-menu  :default-active="this.$route.path" router class="el-menu-vertical-demo" >
    <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name" class="it" >
			<span  style="color:white ; font-size: 16px;" class="wenzi">{{ item.navItem }}</span>
    </el-menu-item>
  </el-menu>
	</el-aside>
</template>

<script lang="ts">
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
export default ({
    data() {
      return {
        navList:[
            {name:'/before',navItem:'文件预览'},
            {name:'/after',navItem:'分割视图'},
            {name:'/pragh',navItem:'数据分析'},
            {name:'/user',navItem:'用户中心'},
        ]
      }
    }

})
</script>
<style scoped>
.mb-2{
	transform:translate(4vw,-5.7vh) ;
	height: 6vh;
	width: 6vw;
}
.el-menu-vertical-demo{
	transform: translate(0,18vh);
}

.el-menu-item {
	--text-color:#fdfdfd;
	background-color: rgb(51, 52, 53);
}
.el-menu-item.is-active {
	--text-color:#fdfdfd;
	background-color: #3f92e0 !important;
}
.it{
  display: flex;
  justify-content: center;
  align-items: center;

}
.el-aside{
width: 14vw;
height: 100vh;
background-color: rgb(51, 52, 53);
position: fixed;
}

</style>

