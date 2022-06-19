<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/img/logo.png" />
    <h1>{{ title }}</h1>
    <button  @click="onGoToPublicationsClicked">Ver las Publicaciones</button>




    <section> <h2>Crear Publicacion desplegable (componente seek/ offer)</h2>
      <button class="seekbutton" @click="onCreateNeedHelpPublicationClicked">Busco ayuda</button>
        <article v-show="isCreateNewSeekForHelpClicked">    
            <NewPublicationComponent  publication_type="0" class="seekhelp"/>   
        </article>

          
      <button class="offerbutton" @click="onCreateOfferHelpPublicationClicked">Quiero ayudar</button>
         <article v-show="isCreateNewOfferOfHelpClicked">
         <NewPublicationComponent  publication_type="1" class="offerhelp"/>
         </article>
    </section>
  
    <section> <h2>Formulario Crear Nuevo Usuario o Loguearse</h2>

      <button class="createuserbutton" @click="onCreateNewUserClicked">Registrarse</button>
        <article v-show="isCreateNewUserClicked">
          <UserFormComponent user_type="new" @sendingNewUser="onSavingNewUser" />   
        </article>
            
      <button class="loginbutton" @click="onLogInUserClicked">Loguearse</button>
        <article v-show="isLogInUserClicked">
          <h2>Seleccionar usuario precargado</h2>
            <select v-model="selectedUser">
              <option :value="null" disabled>Selecciona un usuario</option>
              <option v-for="user in usersList" :value="user" :key="user.id">
                {{user.user_id}} - {{ user.first_name }}  {{ user.last_name }}
              </option>
            </select>
            <button @click="selectingUser">Seleccionar Usuario</button>
        </article>
      </section>
    
  </div>
</template>

<script>
           
import { getUsers, saveNewUser} from "@/services/api.js";

import UserFormComponent  from "@/components/UserForm.vue"
import NewPublicationComponent  from "@/components/NewPublicationComponent.vue"


export default {
  name: 'Home',
  components:{
    UserFormComponent,
    NewPublicationComponent
},
  data() {
    return {
      title: "Welcome",
      publication_list: [],
      isCreateNewSeekForHelpClicked: false,
      isCreateNewOfferOfHelpClicked: false,
      isCreateNewUserClicked: false,
      isLogInUserClicked: false,
      selectedUser: null,
      usersList: []
    }
  },

  mounted() {
     
    
    this.loadData();
    /*
    if (localStorage.getItem('activeUserWatcher')) {
      try {
        this.selectedUser = JSON.parse(localStorage.getItem('activeUserWatcher'));
      } catch(e) {
        localStorage.removeItem('activeUserWatcher');
      }
    }
   **/

  },
  watch: {
    selectedUser:{
      handler(newSelectedUser){
        localStorage.activeUserWatcher = JSON.stringify(newSelectedUser);
      },
      deep: true
    }
  },
  
  methods: {
    async loadData() {
       this.usersList = await getUsers()
    },

    selectingUser() {

      /*
     let parsed = JSON.stringify(this.selectedUser);
      localStorage.setItem('activeUserWatcher', parsed);
      **/
    
      

      console.log("selectedUser HomePage: ", this.selectedUser)
      console.log("localUser HomePage activeUserWatcher: ", localStorage.activeUserWatcher)


     
      alert("usuario seleccionado!")
      // NO funciona
     this.$root.$forceUpdate();
     this.$router.$forceUpdate();//ahora home, luego otra page

      


    },

    onGoToPublicationsClicked() { //no se usa, borrar
      console.log("---> onGoToPublicationsClicked()")

      // 1) Ir a la pagina de contactos
        this.$router.push("/publications");
    },


    onLogInUserClicked() { 
      console.log("clicked: onLogInUserClicked");
      this.isLogInUserClicked = !this.isLogInUserClicked
    },
    onCreateNewUserClicked() {
      console.log("clicked: onCreateNewUserClicked");
      this.isCreateNewUserClicked = !this.isCreateNewUserClicked
    },

    async onSavingNewUser(oneUser){
      console.log("usuario nuevo recibido del hijo: ", oneUser)
   
      console.log("guardando Usuario, first_name usuario:", oneUser.first_name)
      saveNewUser(oneUser)
      alert("Usuario creado!")
    },
    onCreateNeedHelpPublicationClicked(){ //nuevo
            this.isCreateNewSeekForHelpClicked = !this.isCreateNewSeekForHelpClicked

    },
    onCreateOfferHelpPublicationClicked(){ //nuevo
            this.isCreateNewOfferOfHelpClicked = !this.isCreateNewOfferOfHelpClicked

    },




  }


}
</script>

<style scoped>

  .seekhelp {
    color: peru;
    /**En nueva Publicacion se ven los cambios*/

  }
  .offerhelp {
    color: rgb(54, 64, 140); 
    /**En nueva Publicacion se ven los cambios*/
  }

h1 {
  font-style: italic;
}

button {
  border: 2px solid black;
  background-color: white;
  color: black;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  border-color: #04AA6D;
  color: #04AA6D;
  text-shadow: 1px #837c7c;
  min-width: 13em;

}

button:hover {
  background-color: #04AA6D;
  color: white;
}

section {
  margin: 5em;
  display: flex;
  flex-direction: column;
  align-items: center;
}




article {
  
  justify-content: center;
  display: flex;
  flex-direction: column;
  padding: 2em;
  border-radius:1em;
	margin:0 auto;
  /** 
  
	background-color: #fbfbfb;
  border: 1px solid #04AA6D;
   */
  background-color:rgb(214, 218, 221);
  max-width: fit-content;
  }

.goToCreatePubButton {
  max-width: fit-content;
  align-content: center;
  align-self: center;
}
</style>