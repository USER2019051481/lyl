(define (domain Two-piled-Modular-one-blocking-nim)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition  (and (= ?v1 0) (= ?v2 0) (= ?v3 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v3 0)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (or (%= ?k 3 1) (%= ?k 3 2)))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (or (%= ?k 3 1) (%= ?k 3 2)))
        :effect (assign ?v2 (- ?v2 ?k)))
)