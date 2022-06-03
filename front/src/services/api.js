import config from "@/config.js";



export async function getPublications() {
    
    const response = await fetch(`${config.API_PATH}/publications`);
    const pub_list = await response.json();
    return pub_list;
}
  

export async function addPublication(newPub) {
    const settings = {
        method: "POST",
        body: JSON.stringify(newPub),
        headers: {
            "Content-Type": "application/json",
        },
    }
    await fetch(`${config.API_PATH}/publications`, settings);

}
  
export async function getPublicationById(pubId){

    const settings = {
      method: "GET",
      headers: {
      //  JSON application (aun sin user)
      },
    }
   
    const response = await fetch(
      `${config. API_PATH}/publications/${pubId}`,
      settings);

    let publication = await response.json();

    return publication
}

export async function editPublication(publication) {
    const settings = {
      method: "PUT",
      body: JSON.stringify(publication),
      headers: {
        "Content-Type": "application/json",
      },
    };
    await fetch(`${config.API_PATH}/publications/${publication.id_pub}`, settings);
}


export async function deletePublicationById(id_publication) {
  //    body: JSON.stringify(id_publication),

  
  const settings = {
    method: "DELETE",
    body: "",
    headers: {
      "Content-Type": "application/json",
    },
  };
  await fetch(`${config.API_PATH}/publications/${id_publication}`, settings);
}
