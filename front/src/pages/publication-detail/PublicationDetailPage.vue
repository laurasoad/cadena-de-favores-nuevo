<template>
  <h1>Publication detail:  {{ publication.id_pub }} </h1>
  <ul class="pub-item">
      <li>Título: {{ publication.title }}</li>
      <li>Descripción: {{ publication.description }}</li>
      <li>Tipo de publicación: {{ publication.publication_type }}</li>
      <li>Lugar: {{ publication.location }}</li>
      <li>Categoría: {{ nameCat}}</li>
      <li>Etiquetas: {{ publication.tags}}</li>
      <li>Fecha de publicación: {{ publication.date }}</li>
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
      categoriesList:[
            {"category_id":"CAT_GENERAL", "name":"General"}, // añadir imágenes
            {"category_id":"CAT_EDUCATION", "name":"Educación"},
            {"category_id":"CAT_MUSIC", "name":"Música"},
            {"category_id":"CAT_HEALTH", "name":"Salud"}],
      nameCat: "",
       tagsList: [
              {id:1, "name": '#clases'},
              {id:2, "name": '#mates' },
              {id:3, "name": '#online' },
              {id:4, "name": '#piano'}],
    };
  },
  computed: {
      isThisUserTheOwnerOfPublication() {

      if(this.activeUserId != ""){
        return this.activeUserId == this.publication.user_id
      }
      return false
  },

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
      this.getCategoryName();

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
     getCategoryName(){
      let result = this.categoriesList.filter((cat)=> cat.category_id == this.publication.category_id)
      console.log(result[0].name)
      this.nameCat = result[0].name
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