<template>
  <div class="about">
    <h1>This is an about page</h1>
        <img class="logo" alt="Help logo" src="@/assets/img/helplogo.png" />
        <img class="mountain" alt="Mountain logo" src="@/assets/img/helping-hand-silhouette-mountain-moonlight.jpg" />´


  </div>
</template>
<script>
export default {
  data() {
  // otro: "{ backgroundImage: 'url(' + require(`@/assets/${imagepath}`) + ')', width: '300px', height: '200px' }"
  },
}
</script>

<style scoped>
body { 

    background-image: url('~@/assets/img/helping-hand-silhouette-mountain-moonlight.jpg'); 
  
}
.logo {
  border: 1px solid rgb(243, 238, 238);
  border-radius: 40%;
  max-height: 9em;
  max-width: 9em;
  
}
.mountain {
  border-radius: 5px;
  max-height: 30em;
  max-width: 30em;

}

img:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

</style>