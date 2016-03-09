import alt from '../alt';

class QuizActions {
    constructor() {
        this.generateActions(
            'load',
            'nextQuestion',
            'showAnswer',
            'showHint',
            'highlightWord'
        )
    }
}

export default alt.createActions(QuizActions);
