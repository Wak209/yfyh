<template>

  <el-menu :default-active="this.$route.path" router mode="horizontal">
    <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
        {{ item.navItem }}
    </el-menu-item>
  </el-menu>

</template>

<script lang="ts" >
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
export default ({
    data() {
      return {
        navList:[
            {name:'/',navItem:'Home'},
           // {name:'/two',navItem:'2D'},
            {name:'/three',navItem:'3D Segmentation'},
            {name:'/others',navItem:'About'},
        ]
      }
    }

})
</script>

<style>


</style>
