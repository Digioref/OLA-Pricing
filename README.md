# OLA-Pricing
## Status of the Work
| Requirement | Stato di completamento | Note |
| :--- | :--- | :--- |
| 1. Requirement 1: Single product and stochastic environment | ![](https://geps.dev/progress/100) | Rileggere tutto (tutti) |
| 2. Requirement 2: Multiple products and stochastic environment | ![](https://geps.dev/progress/100) | Rileggere tutto (tutti)  |
| 3. Requirement 3: Best-of-both-worlds algorithms with a single product | ![](https://geps.dev/progress/100) | Rileggere tutto (tutti) |
| 4. Requirement 4: Best-of-both-worlds with multiple products | ![](https://geps.dev/progress/100) | Rileggere tutto (tutti) |
| 5. Requirement 5: Slightly non-stationary environments with multiple products | ![](https://geps.dev/progress/100) | Rileggere tutto (tutti) |

## Introduction
This is the repository for the Project of Online Learning Applications in the academic year 2024/2025.
The Project was developed by:
- Carminati Gabriele
- Compagnoni Riccardo Domingo
- De Introna Federico
- Di Giore Francesco
- Fossa' Chiara
The project includes 5 requirements to analyze various algorithms in different scenarios:
1. Single product and stochastic environment
2. Multiple products and stochastic environment
3. Best-of-both-worlds algorithms with a single product
4. Best-of-both-worlds with multiple products
5. Slightly non-stationary environments with multiple products

## General features of the project
The goal of the project is to design online learning algorithms to sell multiple types of products under production constraints.
#### Parameters
- Number of rounds T
- Number of types of products N
- Set of possible prices P (small and discrete set)
- Production capacity B (For simplicity, there is a total number of products B that the company can produce (independently from the specific type of product)
#### Buyer's behavior
- Has a valuation vi for each type of product in N
- Buys all products priced below their respective valuations
#### Interaction
At each round $$t \in T$$:
1. The company chooses which types of product to sell and set price $$p_{i}$$ for each type of product.
2. A buyer with a valuation for each type of product arrives.
3. The buyer buys a unit of each product with price smaller than the product valuation.

## Requirement 1: Single product and stochastic environment
 Build a **stochastic** environment: a distribution over the valuations of a single type of product. Then, build a pricing strategy using UCB1 **ignoring the inventory constraint** and build a pricing strategy extending UCB1 to handle the **inventory constraint**.
 First, we used UCB1 to fulfill the first part of the requirement, achieving **sublinear** regret. Then, we extended the UCB1 to deal with the inventory constraint, achieving also in this case **sublinear** regret.
 <table>
  <tr>
    <td valign="top" align="center">
        <h4>UCB1</h4>
      <img src="data/UCB1_no_budget.png" alt="Screenshot 1" width="400"/>
      <br/>
    </td>
    <td valign="top" align="center">
        <h4>UCB1_with_budget</h4>
      <img src="data/UCB1_with_budget.png" alt="Screenshot 2" width="400"/>
      <br/>
    </td>
  </tr>
</table>

</div>

## Requirement 2: Multiple products and stochastic environment
Build a **stochastic** environment: a joint distribution over the valuations of all the types of products. Build a pricing strategy using Combinatorial-UCB **with the inventory constraint**.
So, the environment includes a **logit-normal** distribution to deal with multiple products and joint valuations. The **Combinatorial UCB** has been extended with **Gaussian Processes (GP)** for the selection of prices.
The regret is **sublinear**.
<table>
  <tr>
    <td valign="top" align="center">
        <h4>CombUCB-GP</h4>
      <img src="data/CombUCB_GP.png" alt="Screenshot 1" width="400"/>
      <br/>
    </td>
  </tr>
</table>

</div>
