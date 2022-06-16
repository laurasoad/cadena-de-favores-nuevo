<template>
  <div class="container">
    <section class="wrap-search">
      <input id="search" type="search" placeholder="Buscar..." v-model="searchData"/>
    </section>
      <br>
     <section class="publication-list">
      <PublicationItem  v-for=" publication in filteredData" :key="publication.id_pub" 
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
        searchData : ""
      }
    },
    mounted() {
      this.loadData()
    },
    methods: {
      async loadData() {
        this.publicationList = await getPublications();
      }
      
    },
      computed: {
        filteredData(){
          
      return this.publicationList.filter((element) => (element.title.toLowerCase().includes(this.searchData.toLowerCase())))
    }
   

  }


  }
</script>

<style scoped>

  body {
    margin: 0 auto;
    /** */
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