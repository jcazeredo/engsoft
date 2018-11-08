-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 08/11/2018 às 02:49
-- Versão do servidor: 10.1.35-MariaDB
-- Versão do PHP: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `engsoft`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cursos`
--

CREATE TABLE `cursos` (
  `id` int(11) UNSIGNED NOT NULL,
  `nome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `cursos`
--

INSERT INTO `cursos` (`id`, `nome`) VALUES
(0, 'Nenhum'),
(7, 'teste');

-- --------------------------------------------------------

--
-- Estrutura para tabela `disciplinas`
--

CREATE TABLE `disciplinas` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(255) NOT NULL,
  `semestre` int(11) NOT NULL,
  `taxa_aprovacao` int(11) NOT NULL,
  `segunda` int(11) NOT NULL,
  `terca` int(11) NOT NULL,
  `quarta` int(11) NOT NULL,
  `quinta` int(11) NOT NULL,
  `sexta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `disciplinas`
--

INSERT INTO `disciplinas` (`id`, `nome`, `semestre`, `taxa_aprovacao`, `segunda`, `terca`, `quarta`, `quinta`, `sexta`) VALUES
(18, 'Física II', 3, 70, 8, 0, 8, 10, 8),
(19, 'Teomag', 5, 80, 17, 0, 17, 0, 0),
(20, 'Física III', 3, 12, 19, 0, 0, 0, 19),
(21, 'Circuitos Elétricos I', 3, 70, 0, 17, 0, 17, 0),
(22, 'Circuitos Elétricos II', 4, 70, 15, 0, 15, 0, 0),
(23, 'Física I', 1, 40, 8, 0, 8, 0, 8);

-- --------------------------------------------------------

--
-- Estrutura para tabela `disciplinas_curso`
--

CREATE TABLE `disciplinas_curso` (
  `id` int(10) UNSIGNED NOT NULL,
  `curso_id` int(11) NOT NULL,
  `disciplina_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `disciplinas_curso`
--

INSERT INTO `disciplinas_curso` (`id`, `curso_id`, `disciplina_id`) VALUES
(20, 5, 23),
(21, 5, 22),
(22, 5, 21),
(23, 5, 18),
(24, 7, 23),
(25, 7, 21),
(26, 7, 20);

-- --------------------------------------------------------

--
-- Estrutura para tabela `historico`
--

CREATE TABLE `historico` (
  `id` int(10) UNSIGNED NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `disciplina_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `historico`
--

INSERT INTO `historico` (`id`, `usuario_id`, `disciplina_id`) VALUES
(33, 1, 20),
(34, 1, 23);

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `privilegio` int(11) NOT NULL,
  `cartao_aluno` varchar(255) NOT NULL,
  `curso_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `senha`, `privilegio`, `cartao_aluno`, `curso_id`) VALUES
(1, 'Admin', '1', 0, '1', 7),
(25, 'Ian', 'ian', 0, '285682', 0);

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Único` (`nome`);

--
-- Índices de tabela `disciplinas`
--
ALTER TABLE `disciplinas`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `disciplinas_curso`
--
ALTER TABLE `disciplinas_curso`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `historico`
--
ALTER TABLE `historico`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`cartao_aluno`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `disciplinas`
--
ALTER TABLE `disciplinas`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de tabela `disciplinas_curso`
--
ALTER TABLE `disciplinas_curso`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de tabela `historico`
--
ALTER TABLE `historico`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
