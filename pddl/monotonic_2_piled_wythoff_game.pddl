(define (domain Monotonic_two_piled_wythoff_game)
    (:objects ?v1 ?v2)
    (:type normal)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 ?v1)))
    (:action take1
        :parameters (?k)
        :precondition (or (and (= ?k 1) (> ?v1 0)) (and (= ?k 2) (> ?v1 1)))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (or (and (= ?k 1) (> ?v2 ?v1)) (and (= ?k 2) (> ?v2 (+ ?v1 1))))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action takeBoth
        :parameters (?k)
        :precondition (and (= ?v1 ?v2) (> ?v1 0))
        :effect (and (assign ?v1 (- ?v1 1)) (assign ?v2 (- ?v2 1))))
)