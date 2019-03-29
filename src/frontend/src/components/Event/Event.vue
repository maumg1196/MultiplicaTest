<template lang="html">
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
        <b-nav-item href="/events">Eventos</b-nav-item>
        <b-nav-item href="/reporters">Reporteros</b-nav-item>
        <b-nav-item href="/types">Tipos de Eventos</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <div class="container">
      <div class="row">
        <div class="col text-left">
          <h2>Evento</h2>

          <div class="row">
            <div class="col">
              <div class="card">
                <div class="card-body">
                  <p>UUID: {{eventUUID}}</p>
                  <p>Nombre: {{ name }}</p>
                  <p>Reporter: {{ reporter }}</p>
                  <p>Descripción: {{ description }}</p>
                  <p>Tipo: {{ type }}</p>
                  <p>Locación: {{ location }}</p>
                  <p>Fecha Unix: {{ datetime }}</p>
                </div>
              </div>
            </div>
          </div>

          <b-button size="sm" variant="primary" :to="{ name:'ListEvent' }">Listado</b-button>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      eventUUID: this.$route.params.eventUUID,
      name: '',
      reporter: '',
      description: '',
      type: '',
      location: '',
      datetime: '',
    }
  },
  methods: {
    getEvent() {
      const path = `http://localhost:8000/events/${this.eventUUID}`

      axios.get(path).then((response) => {
        this.name = response.data.name
        this.reporter = response.data.reporter
        this.description = response.data.description
        this.type = response.data.type
        this.location = response.data.location
        this.datetime = response.data.datetime
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },

  created(){
    this.getEvent()
  }
}
</script>

<style lang="css" scoped>
</style>