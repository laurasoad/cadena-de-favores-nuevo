<template>
  <div id="nav">
    <router-link to="/">Home</router-link>|
    <router-link to="/about">About</router-link>
  <p v-if="this.activeUser != null"> Usuario conectado: {{activeUser.user_id}} - {{activeUser.first_name}} {{activeUser.last_name}}</p>  
    <p v-else> Usuario no conectado</p>  

  </div>
  <router-view />
</template>
<script>
export default {
  data() {
    return {
      // activeUser : JSON.parse(localStorage.getItem("activeUserWatcher")),
      activeUser : {},      

    };
  },
  
  mounted() {
    this.loadUser();
    
  },
  methods: {
    loadUser() {
           //  window.localStorage.removeItem('activeUserWatcher')
        //window.localStorage.setItem('activeUserWatcher')
      // cargar id usuario activo
      this.activeUser = JSON.parse(localStorage.getItem("activeUserWatcher"))
    /**
        if (localStorage.getItem('activeUserWatcher')) {
      try {
        this.activeUser = JSON.parse(localStorage.getItem('activeUserWatcher'));
      } catch(e) {
        localStorage.removeItem('activeUserWatcher');
      }
    }
     */
   
    },
  }
};


  
  
</script>


