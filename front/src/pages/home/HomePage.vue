<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/img/logo.png" />
    <h1>{{ title }}</h1>
    <button  @click="onGoToPublicationsClicked">Go to publication List</button>

    <section>

      <button class="seekbutton" @click="onSeekHelpClicked">Busco ayuda</button>
      <article v-show="isSeekHelpClicked">
        <UserFormComponent help_type="seek" @sendingNewUser="onSavingNewUser" />   
        <button class="goToCreatePubButton" @click="onCreatingNewSeekHelpPublication">
            Crear publicación (seek)</button>
      </article>
            
      <button class="offerbutton" @click="onOfferHelpClicked">Quiero ayudar</button>
      <article v-show="isOfferHelpClicked">
         <UserFormComponent help_type="offer"  @sendingNewUser="onSavingNewUser" /> 
          <button class="goToCreatePubButton" @click="onCreatingNewOfferHelpPublication">
            Crear publicación Offer</button>
      </article>
     
    </section>
  </div>
</template>

<script>
import UserFormComponent from "@/components/UserForm.vue"
export default {
  name: 'Home',
  components:{
    UserFormComponent
  },
  data() {
    return {
      title: "Welcome",
      publication_list: [],
      isSeekHelpClicked: false,
      isOfferHelpClicked: false,
      newUser: {}


    }
  },
  
  methods: {
    onGoToPublicationsClicked() {
      console.log("---> onGoToPublicationsClicked()")

      // this.localUser.id = this.selectedUser.id,
      //this.localUser.name = this.selectedUser.name
      
      // 2) Ir a la pagina de contactos
        this.$root.$forceUpdate();
        this.$router.push("/publications");
    },


    onOfferHelpClicked() {
      console.log("clicked offer");
      this.isOfferHelpClicked = !this.isOfferHelpClicked
    },
    onSeekHelpClicked() {
      console.log("clicked seek");
      this.isSeekHelpClicked = !this.isSeekHelpClicked
    },

    onSavingNewUser(oneUser){
      console.log("usuario nuevo recibido del hijo: ", oneUser)
      this.newUser = oneUser
    },
    onCreatingNewSeekHelpPublication(){
      this.$router.push("/publications/seek");


    },

    onCreatingNewOfferHelpPublication(){
      this.$router.push("/publications/offer");
    }



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
