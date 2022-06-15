<template>
  <h1>Publication detail:  {{ publication.id_pub }} </h1>
  <ul class="pub-item">
    <li>Title: {{ publication.title }}</li>
    <li>Type: {{ publication.publication_type }}</li>
    <li>Description: {{ publication.description }}</li>
    <li>Location: {{ publication.location }}</li>
    <li>Date: {{ publication.date }}</li>
    <li>Categories: {{ publication.categories }}</li>

  </ul>
  <button v-if="isThisUserTheOwnerOfPublication">
    <router-link :to="`/publications/${publication.id_pub}/edit`">Editar</router-link>
    </button>
    <button  v-if="isThisUserTheOwnerOfPublication" @click="erasePublication">Borrar</button>
</template>
<script>

import { getPublicationById, deletePublicationById, getUserId } from "@/services/api.js";

export default {
  name: "PublicationDetail", 
  data() {
    return {
      publication: {},
      activeUserId : "", //JSON.parse(localStorage.getItem("activeUserWatcher"))
    };
  },
  computed: {
      isThisUserTheOwnerOfPublication() {

      if(this.activeUserId != ""){
        return this.activeUserId == this.publication.user_id
      }
      return false
  }
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      let publicationId = this.$route.params.id;
      this.publication = await getPublicationById(publicationId)
      // cargar id usuario activo
      this.activeUserId = getUserId()

    },
    async erasePublication(){
   
      console.log(this.publication)
      console.log(this.publication.id_pub)

      if (confirm("¿Está seguro de que quiere borrar la publicación?")) {
        await deletePublicationById(this.publication.id_pub)
        
        alert("Se ha borrado correctamente")
      } 

    //Redirige a la página de detalles para ver los cambios
    this.$router.push('/publications/');

    },  

    
  }
};
</script>
<style scoped>
h1 {
  font-style: italic;
}
.pub-item {
  list-style: none;
  
  text-align: left;
  padding: 1em;
  border: 2px solid #04AA6D;
  border-radius: 1em;
  margin: 1em;
}


</style>