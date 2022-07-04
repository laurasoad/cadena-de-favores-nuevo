<template>
   <article class="pub-item" v-bind:class="{seek: seekHelpStyle, offer: offerHelpStyle}">

      <section>
        <h4>{{ publication.title }}</h4>
        <p> Categoría: {{ this.publication.category_id}}</p>
        <p>Lugar: {{ publication.location }}</p>
        
      </section>

      <button @click="goToDetailsClicked(publication.id_pub)">
        Detalles 
      </button>

   </article>
</template>

<script>
export default {
  name: "PublicationItem",
  props: {
    publication: {
      type: Object,
      required: true,
    },
  },  
  data() {
      return {
        seekHelpStyle: false,
        offerHelpStyle: false,
        categoriesList2:[
          {"CAT_GENERAL":"General"}, // añadir imágenes
          {"CAT_EDUCATION":"Educación"},
          {"CAT_MUSIC":"Música"},
          {"CAT_HEALTH":"Salud"}],      
        categoriesList:[
            {"category_id":"CAT_GENERAL", "name":"General"}, // añadir imágenes
            {"category_id":"CAT_EDUCATION", "name":"Educación"},
            {"category_id":"CAT_MUSIC", "name":"Música"},
            {"category_id":"CAT_HEALTH", "name":"Salud"}],
        nameCat: ""
    }
    },
    computed: {
      gettingCategoryName() { // No funciona
      let catId = this.publication.category_id
      return this.categoriesList[catId]
  },

  },
    mounted() {
      this.loadStyles();
      //this.getCategoryName();
    },
    methods: {
      loadStyles() {
        if (this.publication.publication_type == 0){
          this.seekHelpStyle = true
        }
        if (this.publication.publication_type == 1){
          this.offerHelpStyle = true
        }
      },
      goToDetailsClicked(receivedId) { 
      console.log("---> onGoToDetailsClicked()")
      let paramsId = `${receivedId}`
      //PROBLEMA
      // Al usarlo en Details page, no redirige a la publicación de MAtch porque toma su propio id (el de la public. detallada)
      //       this.$router.push({ name: 'PublicationDetail', params: { id: `${this.publication.id_pub}`} } )

      this.$router.push({ name: 'PublicationDetail', params: { id: paramsId} } )
      },
      /**
       * 
      getCategoryName(){ // No funciona
      let result = this.categoriesList.filter((cat)=> cat.category_id == this.publication.category_id)
      console.log(result[0].name)
      this.nameCat = result[0].name
    },
       */
    },
};
</script>

<style scoped>
  /**
  Sombra chula sin color
    .pub-item:hover {
       box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
      
    }
  
  No funciona el root en Vue
  :root {
    --main-offer-color:      #6c5ce7;
    --main-seek-color: rgb(212, 130, 48);
  }
  */
  .offer {
    --main-offer-color: black ;
    color:   var(--main-offer-color);
    /**
    ahora
    #81ecec
    antes
    rgb(90, 104, 212);
    border: 2px solid  var(--main-offer-color);
    ; */
  }

  
  .offer:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  }

  .offer button {
    --main-offer-color:       #00cec9;
    border: 2px solid  var(--main-offer-color);
    background-color: white;
    padding: 14px 28px;
    font-size: 16px;
    cursor: pointer;
    background-color: var(--main-offer-color);
    color: white;  
    text-shadow: 1px #837c7c;
    border-radius: 0.5em;

  }

  
  .offer button:hover {
    --main-offer-color: #00cec9;
    color: var(--main-offer-color);
    background-color: white;
    border-color:  var(--main-offer-color); 
  }

  .seek {
    color: -main-seek-color;
    /**
    border: 2px solid -main-seek-color;
    
    */ 
  }
  .seek:hover {
    box-shadow: 0 8px 16px 0 rgba(182, 17, 17, 0.2);
  }

  .seek button {
    /**
        border: 2px solid  rgb(212, 130, 48);
          #fab1a0
    */
    border: 2px solid   #fab1a0;
    background-color: white;
    padding: 14px 28px;
    font-size: 16px;
    cursor: pointer;
    background-color:  #fab1a0;
    color: white;
    text-shadow: 1px #837c7c;
    border-radius: 0.5em;
  }

  
  .seek button:hover {
    color:  #fab1a0;
    background-color: white;
    border-color:  #fab1a0;
  }


  .pub-item {
    flex: 1 1 21rem;
    /* border: 2px solid #04AA6D; 
    **/
    border-radius: 1em;
    margin: 1em 2em;
    padding: 1em 2em;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-self: normal;
    max-width: 14em;
    /**falta añadir flex para que el espacio se reparta entre section y button */


  }




  button {
  border: 2px solid #04AA6D;
  background-color: white;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  background-color: #04AA6D;
  color: white;
  
  text-shadow: 1px #837c7c;
  border-radius: 0.5em;
}

button:hover {
  color: #04AA6D;
  background-color: white;
  border-color: #04AA6D;

  
}


</style>
