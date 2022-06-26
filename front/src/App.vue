
<template >
  <div id="nav">

    <router-link to="/">Home</router-link> | 
    <router-link to="/about">About</router-link> | 
    <router-link v-if="this.activeUser != null" to="/dashboard">Dashboard</router-link>

    <p v-if="this.activeUser != null"> 
  Usuario conectado: {{activeUser.user_id}} - {{activeUser.first_name}} {{activeUser.last_name}}</p>  
    <p v-else> Usuario no conectado</p>  


  </div>
  <router-view />
</template>


<script>

export default {
  data() {
    return {
      activeUser : null,      

    };
  },
  
  mounted() {
    this.loadUser();
    
  },
    watch: {
    activeUser:{
      handler(newActiveUser){
        console.log("cambio detectado desde App.vue")
        localStorage.activeUserWatcher = JSON.stringify(newActiveUser);
      },
      deep: true
    }
  },
  methods: {
    loadUser() {
           //  window.localStorage.removeItem('activeUserWatcher')
        //window.localStorage.setItem('activeUserWatcher', JSON.stringify(this.selectedUser))
      // cargar id usuario activo
        let extraer = JSON.parse(localStorage.getItem('activeUserWatcher'))
       // let enviar = localStorage.setItem('activeUserWatcher', JSON.stringify(this.selectedUser))
        if (localStorage.getItem('activeUserWatcher')) {
          console.log("extraer ", extraer) // si no hay, es null <___________
      //    console.log(enviar)
      try {
        // extraer GET
        this.activeUser = JSON.parse(localStorage.getItem('activeUserWatcher'));
      } catch(e) {
        console.log("error, cual?", e)
        //  localStorage.removeItem('activeUserWatcher');
      }}
      

   
    },
  }
};


  
  
</script>


