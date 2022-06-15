<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/img/logo.png" />
    <h1>{{ title }}</h1>
    <button  @click="onGoToPublicationsClicked">Ver las Publicaciones</button>




    <section> <h2>Crear Publicacion desplegable (componente seek/ offer)</h2>
      <button class="seekbutton" @click="onCreateNeedHelpPublicationClicked">Busco ayuda</button>
        <article v-show="isCreateNewSeekForHelpClicked">    
            <NewPublicationComponent  publication_type="0"/>   
        </article>

          
      <button class="offerbutton" @click="onCreateOfferHelpPublicationClicked">Quiero ayudar</button>
         <article v-show="isCreateNewOfferOfHelpClicked">
         <NewPublicationComponent  publication_type="1"/>
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
      newUser: {}, // Para cuando se puedan registrar los usuarios
      selectedUser: null,
      // retrievedUser: {}, // PARA LA SOLUCION_01
      usersList: []
    }
  },
  mounted() {
    
    this.loadData();
   

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
      
      // 1) Seleccionar usuario y recargar para guardar en local Storage
      /** SOLUCION CLASICA_00
       localStorage.user_id = this.selectedUser.user_id,
      localStorage.first_name = this.selectedUser.first_name,
      localStorage.last_name = this.selectedUser.last_name,
      localStorage.email = this.selectedUser.email

      console.log("localUser HomePage first name: ", localStorage.first_name)

       */
      
      /**
       * --> SOLUCION_01
       localStorage.setItem('activeUser', JSON.stringify(this.selectedUser))//stringify object and store
      this.retrievedUser= JSON.parse(localStorage.getItem('activeUser')) //retrieve the object
      console.log("retrievedUser", this.retrievedUser)
       */



      this.$root.$forceUpdate();
 

      console.log("selectedUser HomePage: ", this.selectedUser)
      console.log("localUser HomePage activeUserWatcher: ", localStorage.activeUserWatcher)


     
      alert("usuario seleccionado!")
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
      this.newUser = oneUser
      console.log("guardando ", oneUser)
      saveNewUser(oneUser)
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
.seekbutton, .offerbutton {
    color: red;
}



article {
  
  justify-content: center;
  display: flex;
  flex-direction: column;
  padding: 2em;
  border-radius:1em;
	margin:0 auto;
	background-color:rgb(221, 214, 214);
  max-width: fit-content;
  }

.goToCreatePubButton {
  max-width: fit-content;
  align-content: center;
  align-self: center;
}
</style>