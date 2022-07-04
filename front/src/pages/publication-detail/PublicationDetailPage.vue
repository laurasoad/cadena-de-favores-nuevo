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
     <br>
    <button  v-if="isThisUserTheOwnerOfPublication" @click="matching">Match</button>
    <section  class="match-list" v-show="isMatchClicked">
    Hola Match
      <PublicationItem v-for=" publication in filteredMatchList" :key="publication.id_pub" 
      :publication="publication"/>
    </section>
</template>
<script>

import { getPublications, getPublicationById, deletePublicationById, getUserId } from "@/services/api.js";
import PublicationItem from "../../components/PublicationItem.vue";


export default {
  name: "PublicationDetail", 
  components: {
      PublicationItem
    },
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
      publicationList: [],
      isMatchClicked: false
    };
   
  },
  computed: {
      isThisUserTheOwnerOfPublication() {

      if(this.activeUserId != ""){
        return this.activeUserId == this.publication.user_id
      }
      return false
  },
  filteredMatchList(){
          let result = this.publicationList.filter((item)=> this.isDifferentType(item))
                            .filter((item) => this.hasTheSameCategory(item))
                            .filter((item) => this.hasAtLeastTwoTagsInCommon(item) )

          return result
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
      // cargar la lista de publicaciones para Match
      this.publicationList = await getPublications();
      console.log(this.publicationList)


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
     isDifferentType(item) {
          //  console.log("item of list) - publication type ",  item.publication_type )               
          // Si la publicación detallada es del tipo 0 (buscar ayuda)
            if (this.publication.publication_type  == 0){
              // Devuelve las del tipo contrario (ofrecer ayuda, 1)
                return item.publication_type == 1
            } else{
                return item.publication_type == 0 
            }
            
    },
    hasTheSameCategory(item) {
          return item.category_id == this.publication.category_id
     
    },
    hasAtLeastTwoTagsInCommon(item) {
        let commonTagsList =[]           
        for(let indexPub in item.tags){
             // console.log("TAGs del item de la lista ", item.tags) 
             // console.log("TAGs de la publicación detallada ", this.publication.tags) 

             // console.log("TAG ", item.tags[indexPub]) 
              
            for (let index in this.publication.tags){
               //   console.log("TAG item lista", item.tags[indexPub]) 
              //  console.log("TAG pub detallada ", this.publication.tags[index]) 
              //    console.log("match? ", this.publication.tags[index] ==  item.tags[indexPub])
                  if (this.publication.tags[index] ==  item.tags[indexPub]){ 

                        commonTagsList.push( item.tags[indexPub])
                        console.log("commonTagsList", commonTagsList)
                  }
            }
        }
        return commonTagsList.length >= 2
    },
    matching(){
            this.isMatchClicked = !this.isMatchClicked

    }
  

      

    
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