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
          <h2>Eventos de Tipo: {{name}}</h2>

          <div class="col-md-12">
            <div class="overflow-auto">
              <b-pagination
                v-model="currentPage"
                :total-rows="rows"
                :per-page="perPage"
                aria-controls="my-table"
              ></b-pagination>
            </div>
            <b-table 
              striped hover 
              :items="events"
              :fields="fields"
              :per-page="perPage"
              :current-page="currentPage">
            </b-table>
            <b-button size="sm" variant="primary" :to="{ name:'ListEventType' }">Listado</b-button>
          </div>

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
      perPage: 5,
      currentPage: 1,
      typeID: this.$route.params.typeID,
      name: '',
      fields: [
        { key: 'uuid', label: 'UUID'},
        { key: 'name', label: 'Nombre'},
        { key: 'reporter', label: 'Reportero'},
        { key: 'description', label: 'Descripción'},
        { key: 'location', label: 'Locación'},
        { key: 'datetime', label: 'Fecha Unix'},
      ],
      events: [],
    }
  },
  methods: {
    getEvents () {
      const path = `http://localhost:8000/types/${this.typeID}`
      axios.get(path).then((response) => {
        this.events = response.data.events
        this.name = response.data.name
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  computed: {
    rows() {
      return this.events.length
    }
  },

  created(){
    this.getEvents()
  }
}
</script>

<style lang="css" scoped>
</style>