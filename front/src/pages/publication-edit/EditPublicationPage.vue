<template>

<section>
  <h1>Nueva Publicación</h1>

  <form>
    <label for="title">Título:</label>
    <input type="text" key="title" v-model="modifiedPublication.title"/>

    <label for="pub_type">Tipo de publicación:</label>
    <input type="text" key="pub_type" v-model="modifiedPublication.publication_type" disabled/>

    <label for="description">Descripción:</label>
    <textarea id="description" v-model="modifiedPublication.description">
      Descripción:</textarea>

    <label for="location">Lugar:</label>
    <input type="text" id="location" v-model="modifiedPublication.location"/>

    <label for="creation_date">Fecha de creación:</label>
    <input type="text" id="creation_date" v-model="modifiedPublication.date" disabled/>

    <label for="categories">Categorías:</label>
    <input type="text" id="categories" v-model="modifiedPublication.categories"/>
    
    <button @click.prevent="changePublication">Editar Publicación</button>
  </form>

</section>
  

</template>

<script>
import { getPublicationById, editPublication } from "@/services/api.js";

export default {
    name: "EditPublicationPage",
    data() {
        return {
            publication: {},
            modifiedPublication:{}
        }
    }, 
    mounted() {
    this.loadData();
    },
    methods: {
      async loadData() {
        let publicationId = this.$route.params.id;
        this.publication = await getPublicationById(publicationId)

      // Creamos la variable "modifiedPublication" con 2 objetivos:
      // 1 - Cuando se carga la página: Para mostrar los datos de la publicación
      // 2 - Para comprobar si el usuario ha editado algo:
      //     comparando los datos de  "publication" y modifiedPublication"

      this.modifiedPublication.id_pub = this.publication.id_pub;
      this.modifiedPublication.publication_type = this.publication.publication_type;
      this.modifiedPublication.title = this.publication.title;
      this.modifiedPublication.description = this.publication.description;
      this.modifiedPublication.location = this.publication.location;
      this.modifiedPublication.date = this.publication.date;
      this.modifiedPublication.categories = this.publication.categories;

      },
      isEmpty() {
      return (
        this.modifiedPublication.title === "" ||
        this.modifiedPublication.description === "" ||
        this.modifiedPublication.location === ""
      );
    },

      isModified() {
      return (
          this.publication.title != this.modifiedPublication.title ||
          this.publication.description != this.modifiedPublication.description ||
          this.publication.location != this.modifiedPublication.location ||
          this.publication.categories != this.modifiedPublication.categories
        );
      },

      async changePublication(){
        if(this.isEmpty()){
          alert("Error! Rellene todos los campos, por favor")

        }else {
          if(this.isModified()){
            console.log(this.modifiedPublication)
            if (confirm("¿Está seguro de que quiere editar la publicación?")) {
              await editPublication(this.modifiedPublication);
             
              alert("Los cambios se han guardado correctamente")
            } 

          //Redirige a la página de detalles para ver los cambios
          this.$router.push(`/publications/${this.publication.id_pub}`);
      
        } else { 
          alert("No se ha modificado ningún dato");
        }
        }
        

      }

   
    }

}
</script>

<style scoped>
section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

h1{
  /**
    color: #ab4493;  color bonito

  */
  font-size: 2em;  
  color: #ab4493;
}


form {  
  box-sizing: border-box;
  margin: 1em;
  border-radius: 0.5em;
  float: center;
  padding: 1em 1em 1em 1em;
  background-color: #fbfbfb; 
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}


input{
  background-color: #fbfbfb; 
  width: 75%; 
  min-width: 20em;

  height: 2.5em; 
  border: 1px solid #04AA6D;
  border-radius: 5px;  
  padding-left: 0.1em;
  margin-top: 0.2em;  
  margin-bottom: 0.8em; 
}


textarea{
  background-color: #fbfbfb; 
  width: 74%; 
  min-width: 20em;

  height: 150px; 
  border-radius: 5px;  
  border: 1px solid #04AA6D;
  margin-top: 0.2em;  
  margin-bottom: 0.8em; 
  
}


label{
  display: block; 
  float: center;  
}


button{
  height: 45px; 
  padding-left: 5px;
  padding-right: 5px;   
  margin-bottom: 20px; 
  margin-top: 10px;   
  text-transform: uppercase;
  background-color: #04AA6D; 
  border-color: #04AA6D; 
  border-style: solid; 
  border-radius: 10px;  
  width: 75%;   
  min-width: 20.2em;
  cursor: pointer;
  color:#fbfbfb
}


form input:focus{
  outline:0;
  border: 1px solid #97d848;
}


form textarea:focus{
  outline:0;
  border: 1px solid #97d848;
}







</style>