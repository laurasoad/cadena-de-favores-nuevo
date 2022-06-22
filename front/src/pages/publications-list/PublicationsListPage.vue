<template>
  <div class="container">
    <section class="wrap-search">
      <input id="search" type="search" placeholder="Busca un título, descripción o lugar" v-model="textSearched"/>
    </section>
    <select v-model="selectedCategory">
      <option disabled>Filtrar por categoría</option>
      <option v-for="category in categoriesList" :value="category.category_id" :key="category.category_id">
                {{ category.name}} 
      </option>
    </select>
     <select v-model="selectedType">
      <option disabled>Filtrar por tipo de publicación</option>
      <option v-for="item in publicationTypeList" :value="item.type" :key="item.type">
                {{ item.name}} 
      </option>
    </select>
      <br>
     <section class="publication-list">
      <PublicationItem  v-for=" publication in filteredList" :key="publication.id_pub" 
      :publication="publication"/>
     </section>
  </div>
</template>

<script>
  // mejora: import { getPublications } from '@/services/api.js'
  import PublicationItem from "./PublicationItem.vue";
  import { getPublications } from "@/services/api.js";



  export default {
     
    name: 'PublicationList',
    components: {
      PublicationItem
    },
    data() {
      return {
        publicationList: [],
        textSearched : "",
        categoriesList:[
              {"category_id":"CAT_ALL", "name":"Todas las categorías"}, 
              {"category_id":"CAT_GENERAL", "name":"General"}, 
              {"category_id":"CAT_EDUCATION", "name":"Educación"},
              {"category_id":"CAT_MUSIC", "name":"Música"},
              {"category_id":"CAT_HEALTH", "name":"Salud"}],
        publicationTypeList:[
              {"type": "0", "name":"Buscar ayuda"}, 
              {"type": "1", "name":"Ofrecer ayuda"}, 
              {"type": "2", "name":"Todos los tipos"}],
        selectedCategory: '',
        selectedType: ''
      
      }
    },
    mounted() {
      this.loadData()
    },
      computed: {
        filteredList(){
          let result = this.publicationList.filter((item)=> this.isFilteredByText(item))
                            .filter((item)=> this.isFilteredByCategory(item))
                            .filter((item)=> this.isFilteredByType(item))
          return result
      }
    },
    methods: {
      async loadData() {
        this.publicationList = await getPublications();
      },
        isFilteredByText(item) {
            return item.title.toLowerCase().includes(this.textSearched.toLowerCase())||
                    item.description.toLowerCase().includes(this.textSearched.toLowerCase()) ||
                    item.location.toLowerCase().includes(this.textSearched.toLowerCase()) 
        },
         isFilteredByCategory(item) {
          
            if (this.selectedCategory == ""){ 
                return true
            }
            if (this.selectedCategory.includes("CAT_ALL")){
                return true
            } else{
                
                return this.selectedCategory.includes(item.category_id)
            }
            
        },
        isFilteredByType(item) {
            console.log("selected ", this.selectedType)
            console.log("item ",  item.publication_type )               
            console.log(item.publication_type == this.selectedType)
            
            if (this.selectedType == ""){ 
                return true
            }
            if (this.selectedType.includes("2")){
                return true
            } else{
                return this.selectedType.includes(item.publication_type) 
            }
            
        }
    }}
  

   /**
    * 
    * 
      return this.publicationList.filter((element) => {(element.title.toLowerCase().includes(this.textSearched.toLowerCase()))
                                                   ||(element.description.toLowerCase().includes(this.textSearched.toLowerCase())) }  )
    
             filteredList(){
          this.publicationList.filter((element) => {
             let isTitleIncluded = element.title.toLowerCase().includes(this.textSearched.toLowerCase())
             let isDescriptionIncluded = element.title.toLowerCase().includes(this.textSearched.toLowerCase())
             return isTitleIncluded || isDescriptionIncluded
             })

        }
          
            */
          
      
   //   const results = people.filter(element => {
  // 👇️ using AND (&&) operator
 // return element.age === 30 && element.name === 'Carl';
</script>

<style scoped>

  body {
    margin: 0 auto;
    font-family: 'Nunito Sans';
    background-color: #f2f2f2;
    }

    #search{
      background-color: #fbfbfb; 
      width: 75%; 

      height: 2.5em; 
      border: 1px solid black;
      border-radius: 5px;  
      padding-left: 0.1em;
      margin-top: 0.2em;  
      margin-bottom: 0.8em; 
      padding: 1.5em;
    }
    #search:hover {
      border: 1.5px solid black;
      /** 
      box-shadow: 0 7px 15px 0 rgba(0,0,0,0.1);

       */


    }

  h1 {
    font-style: italic;
  }

  .publication-list {
    display: flex;        
   /* flex-flow: row wrap; interesante para que vaje a
   la siguiente fila si no hay sitio*/
   flex-flow: row wrap; 


    margin: 0 auto;
    align-items: center;
    justify-content: space-evenly;


  }


</style>