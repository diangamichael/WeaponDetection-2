import { Route, Switch } from 'react-router-dom'
import AppInfo from './AppInfo'
import Home from './Home'

export default function Routes() {
    return (
        <Switch>
            <Route exact path='/'>
                <Home/>
            </Route>
            <Route exact path='/info'>
                <AppInfo />
            </Route>
        </Switch>
    )
}