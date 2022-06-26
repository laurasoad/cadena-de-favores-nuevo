<template>
  <div class="about">
    <h1>About us</h1>
    <!--
        <img class="mountain" alt="Mountain logo" src="@/assets/img/helping-hand-silhouette-mountain-moonlight.jpg" />´
          <section>
      <h3>
        ¿Quiénes somos?
      </h3>
    </section>

    -->
   <img class="dog" alt="About us - dog in the keyboards" src="https://images.unsplash.com/photo-1589652717406-1c69efaf1ff8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80" />´
  


  </div>
</template>
<script>
export default {
  data() {
  // otro: "{ backgroundImage: 'url(' + require(`@/assets/${imagepath}`) + ')', width: '300px', height: '200px' }"
  
  //      <img class="mountain" alt="Mountain logo" src="@/assets/img/helping-hand-silhouette-mountain-moonlight.jpg" />´

  },
}
</script>

<style scoped>
body { 
  /**
      background-image: url('~@/assets/img/helping-hand-silhouette-mountain-moonlight.jpg'); 
    background-image: url('./src/assets/img/logo.png'); 

  */
  
}
.logo {
  border: 1px solid rgb(243, 238, 238);
  border-radius: 40%;
  max-height: 9em;
  max-width: 9em;
  
}
.dog {
  border-radius: 5px;
  max-height: 30em;
  max-width: 30em;

}

img:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

</style>