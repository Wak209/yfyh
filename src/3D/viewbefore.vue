<script>
import {Niivue} from '@niivue/niivue'
const nv = new Niivue()


export default {
  name: 'App',
  props: {

  },
  data(){
    return {
      volumeList: [
        {
          url: "/before.nii.gz",
        },
      ]

    }
  },

  mounted(){
    nv.attachTo('gl');
    nv.loadVolumes(this.volumeList);
  }
}

</script>

<template>
    <div class="conv">
        <canvas id="gl"></canvas>
    </div>

</template>

<style lang="less" scoped>
.conv{
    width: 80vw;
}
</style>