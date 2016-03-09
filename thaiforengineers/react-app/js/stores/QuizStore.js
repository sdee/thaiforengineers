import alt from '../alt';
import QuizActions from '../actions/QuizActions';

class QuizStore {
    constructor() {
        this.bindActions(QuizActions);
        this.cards = [];
        this.currCardIdx = 0;
    }

    onLoad(){

    }

    onNextQuestion(){

    }

    onShowAnswer(){

    }

    onShowHint(){

    }

    onHighlightWord(){

    }
}

export default alt.createStore(QuizStore);