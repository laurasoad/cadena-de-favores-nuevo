<template>
  <div class="dashboard">
    <!--

      <h1>Hola {{ selectedUser.first_name}}</h1>
    -->
    <button  @click="onGoToPublicationsClicked">Ver las Publicaciones</button>

    <section> <h2>Crear Publicación</h2>
      <button class="seekbutton" @click="onCreateNeedHelpPublicationClicked">Busco ayuda</button>
        <article v-show="isCreateNewSeekForHelpClicked">    
            <NewPublicationComponent  publication_type="0" class="seekhelp"/>   
        </article>

          
      <button class="offerbutton" @click="onCreateOfferHelpPublicationClicked">Quiero ayudar</button>
         <article v-show="isCreateNewOfferOfHelpClicked">
         <NewPublicationComponent  publication_type="1" class="offerhelp"/>
         </article>
    </section>
  
  
  </div>
</template>

<script>
           

import NewPublicationComponent  from "@/components/NewPublicationComponent.vue"


export default {
  name: 'Dashboard',
  components:{
    NewPublicationComponent
},
  data() {
    return {
      
      publication_list: [],
      isCreateNewSeekForHelpClicked: false,
      isCreateNewOfferOfHelpClicked: false,
      selectedUser : localStorage.getItem("activeUserWatcher"),
    }
  },

  mounted() {

  },

  
  methods: {



    onGoToPublicationsClicked() {
      // 1) Ir a la pagina de contactos
        this.$router.push("/publications");

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

<style scoped>´
.dashboard{ 
  /** para modal, css del fondo */
    display: none;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    position: fixed;
    background-color: rgba(0,0,0,0.8);
    z-index: 2;
}
.logo {
  border: 3px solid rgb(182, 49, 49);
  border-radius: 40%;
  max-height: 9em;
  max-width: 9em;
  
}

img:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

/*
 En nueva Publicacion se ven los cambios
  .seekhelp {
    color: peru;
   

  }
  .offerhelp {
    color: rgb(54, 64, 140); 
  
  }
*/


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