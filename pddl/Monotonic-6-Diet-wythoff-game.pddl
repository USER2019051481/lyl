(define (domain Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v2 ?v1)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (or (= ?k 1) (= ?k 2) (= ?k 3) (= ?k 4) (= ?k 5) (= ?k 6)))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (or (and (= ?k 1) (> ?v2 ?v1)) (and (= ?k 2) (> ?v2 (+ ?v1 1))) (and (= ?k 3) (> ?v2 (+ ?v1 2)))  (and (= ?k 4) (> ?v2 (+ ?v1 3))) (and (= ?k 5) (> ?v2 (+ ?v1 4))) (and (= ?k 6) (> ?v2 (+ ?v1 5))) )
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (= ?v1 ?v2) (= ?k 1))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?k))))
)