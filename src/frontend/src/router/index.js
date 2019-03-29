import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListEvent from '@/components/Event/ListEvent'
import ListReporter from '@/components/Reporter/ListReporter'
import ListEventType from '@/components/Event/ListEventType'
import Event from '@/components/Event/Event'
import Reporter from '@/components/Reporter/Reporter'
import EventType from '@/components/Event/EventType'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/events',
      name: 'ListEvent',
      component: ListEvent
    },
    {
      path: '/reporters',
      name: 'ListReporter',
      component: ListReporter
    },
    {
      path: '/types',
      name: 'ListEventType',
      component: ListEventType
    },
    {
      path: '/events/:eventUUID',
      name: 'Event',
      component: Event
    },
    {
      path: '/reporters/:reporterID',
      name: 'Reporter',
      component: Reporter
    },
    {
      path: '/types/:typeID',
      name: 'EventType',
      component: EventType
    },
  ],
  mode: 'history'
})
